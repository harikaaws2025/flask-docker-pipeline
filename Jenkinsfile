pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
        IMAGE_NAME = "harika112/flask-docker-pipeline"
        APP_PORT = "5000"
        CONTAINER_NAME = "flask_app_live"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'dockerhub-creds', url: 'https://github.com/harikaaws2025/flask-docker-pipeline.git']])
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
                    sh 'docker rm -f test_container || true'
                    sh 'docker run -d -p ${APP_PORT}:${APP_PORT} --name test_container $IMAGE_NAME:latest'
                    sleep(15)
                    sh 'curl -f http://localhost:${APP_PORT} || (echo "Container test failed" && exit 1)'
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

        stage('Deploy to Local') {
            steps {
                script {
                    echo "🚀 Deploying Flask app container locally..."
                    // Stop old running instance if any
                    sh 'docker rm -f $CONTAINER_NAME || true'
                    // Start new container persistently
                    sh 'docker run -d -p ${APP_PORT}:${APP_PORT} --name $CONTAINER_NAME $IMAGE_NAME:latest'
                }
            }
        }
    }

    post {
        success {
            echo "✅ App is now deployed and running!"
            echo "🌐 Access it at: http://<your-server-ip>:${APP_PORT}"
        }
    }
}
