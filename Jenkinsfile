pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')  // Jenkins credentials ID
        IMAGE_NAME = "yourdockerhubusername/flask-docker-pipeline"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/yourusername/flask-docker-pipeline.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:latest .'
            }
        }

        stage('Test Container') {
            steps {
                script {
                    sh 'docker run -d -p 1234:5000 --name test_container $IMAGE_NAME:latest'
                    sleep(5)
                    sh 'curl -f http://localhost:5000 || (echo "Container test failed" && exit 1)'
                    sh 'docker stop test_container && docker rm test_container'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                    sh 'docker push $IMAGE_NAME:latest'
                }
            }
        }
    }

    post {
        always {
            sh 'docker system prune -f'
        }
        success {
            echo "✅ Build, Test, and Push Successful!"
        }
        failure {
            echo "❌ Pipeline Failed!"
        }
    }
}
