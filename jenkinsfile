pipeline {
    agent any

    environment {
        IMAGE_NAME = 'stock-backend'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/girishn7/dev.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl apply -f k8s/backend-deployment.yaml
                kubectl apply -f k8s/backend-service.yaml
                '''
            }
        }
    }
}
