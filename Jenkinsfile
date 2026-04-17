pipeline {
    agent any

    environment {
        PYTHON_VENV = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                python3 -m venv ${PYTHON_VENV}
                . ${PYTHON_VENV}/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                . ${PYTHON_VENV}/bin/activate
                python -m unittest discover tests -v
                '''
            }
        }

        stage('Mock Deployment') {
            steps {
                echo 'Deploying to staging environment...'
                echo 'Application deployed successfully!'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Success! Your EdTech app is ready.'
        }
        failure {
            echo 'Pipeline failed. Check the logs.'
        }
    }
}
