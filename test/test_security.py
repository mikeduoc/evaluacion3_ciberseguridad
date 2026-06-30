import pytest

from app.app import app
from app.secure_sql import init_db, get_user_info
from app.secure_command import run_command
from app.secure_deserialization import load_data


def test_xss_input_is_escaped():
    with app.test_client() as client:
        response = client.get("/", query_string={
            "input": "<script>alert(1)</script>"
        })

        body = response.get_data(as_text=True)

        assert response.status_code == 200
        assert "<script>" not in body
        assert "&lt;script&gt;" in body


def test_sql_injection_payload_does_not_return_admin(tmp_path):
    db_path = tmp_path / "users.db"
    init_db(db_path)

    malicious_input = "admin' OR '1'='1"
    result = get_user_info(malicious_input, db_path)

    assert result == []


def test_command_injection_is_blocked():
    with pytest.raises(ValueError):
        run_command("whoami && hostname")


def test_allowed_command_runs():
    result = run_command("hostname")
    assert isinstance(result, str)


def test_json_deserialization_valid_file(tmp_path):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    file_path = data_dir / "ejemplo.json"
    file_path.write_text('{"usuario": "admin"}', encoding="utf-8")

    result = load_data("ejemplo.json", data_dir)

    assert result["usuario"] == "admin"


def test_path_traversal_is_blocked(tmp_path):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    with pytest.raises(ValueError):
        load_data("../secreto.json", data_dir)