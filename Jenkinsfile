pipeline {
    agent any

    environment {
        IMAGE_NAME = 'stock-backend'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                dir('backend') {    // 👈 Telling Jenkins to move into backend/ folder
                    script {
                        docker.build("${IMAGE_NAME}")
                    }
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
