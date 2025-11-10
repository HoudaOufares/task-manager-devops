pipeline{
    agent any

    stages{
        stage('Checkout'){
            steps{
                echo 'Code cloné depuis GitHub'
            }
        }

        stage('Test'){
            steps{
                echo 'Running automated tests with pytest...'
                sh '''
                  python3 -m venv venv 
                  . venv/bin/activate 
                  pip install -r requirements.txt
                  python3 -m pytest tests/ -v
                '''
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