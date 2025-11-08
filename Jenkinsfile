pipeline{
    agent any

    stages{
        stage('Checkout'){
            steps{
                echo 'Code cloné depuis GitHub'
            }
        }

        stage('Build Docker Image'){
            steps{
                echo ' Building Docker image...'
                script{
                    sh 'echo "Image Docker déjà créée: task-manager:v1"'
                }
            }
        }

        stage('Deploy to  Kubernetes'){
            steps{
                echo 'Deploying to Kubernetes...'
                sh 'echo "kubectl apply -f k8s/"'
            }
        }

    }
}