pipeline {
    agent any

    environment {
        IMAGE_NAME = 'stock-backend'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                dir('backend') {
                    script {
                        docker.build("${IMAGE_NAME}")
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat '''
                kubectl apply --validate=false -f k8s/backend-deployment.yaml
                kubectl apply --validate=false -f k8s/backend-service.yaml
                '''
            }
        }
    }
}
