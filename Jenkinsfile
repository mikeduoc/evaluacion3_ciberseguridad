pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Construccion Docker') {
            steps {
                bat 'docker build -t ev3-secure-app:%BUILD_NUMBER% .'
            }
        }

        stage('Pruebas unitarias') {
            steps {
                bat 'docker run --rm ev3-secure-app:%BUILD_NUMBER% pytest -q'
            }
        }

        stage('Revision SAST con Bandit') {
            steps {
                bat 'docker run --rm ev3-secure-app:%BUILD_NUMBER% bandit -r app -ll'
            }
        }

        stage('Auditoria de dependencias') {
            steps {
                bat 'docker run --rm ev3-secure-app:%BUILD_NUMBER% pip-audit -r requirements.txt || exit /b 0'
            }
        }

        stage('Despliegue local') {
            steps {
                bat 'docker rm -f ev3-secure-app-running || exit /b 0'
                bat 'docker run -d --name ev3-secure-app-running -p 5000:5000 ev3-secure-app:%BUILD_NUMBER%'
                bat 'timeout /t 5'
                bat 'curl -f http://localhost:5000/'
            }
        }

        stage('OWASP ZAP Baseline Scan') {
            steps {
                bat '''
                docker run --rm ^
                -v "%cd%:/zap/wrk:rw" ^
                ghcr.io/zaproxy/zaproxy:stable ^
                zap-baseline.py ^
                -t http://host.docker.internal:5000 ^
                -r zap_report.html || exit /b 0
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'zap_report.html', allowEmptyArchive: true
        }
    }
}