pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
        IMAGE_NAME = "harika112/flask-docker-pipeline"
        APP_PORT = "5000"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'dockerhub-creds', url: 'https://github.com/harikaaws2025/flask-docker-pipeline.git']])
            }
        }

        stage('Verify Docker Access') {
            steps {
                sh 'docker info'
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
                    echo "🧹 Removing old test containers (if any)..."
                    sh 'docker rm -f test_container || true'

                    echo "🚀 Starting new test container..."
                    sh 'docker run -d -p ${APP_PORT}:${APP_PORT} --name test_container $IMAGE_NAME:latest'

                    echo "⏳ Waiting for Flask app to start..."
                    sleep(15)

                    sh 'docker ps'
                    sh 'docker logs test_container'

                    echo "🔍 Checking app health..."
                    sh 'curl -f http://localhost:${APP_PORT} || (echo "Container test failed" && exit 1)'

                    echo "🧹 Cleaning up test container..."
                    sh 'docker stop test_container && docker rm test_container'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    echo "🔐 Logging into DockerHub..."
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'

                    echo "📦 Pushing image to DockerHub..."
                    sh 'docker push $IMAGE_NAME:latest'
                }
            }
        }
    }

    post {
        always {
            echo "🧽 Cleaning Docker system..."
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
