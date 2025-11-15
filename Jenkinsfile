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
            script {
            sh 'docker build -t houdaoufares620/task-manager:v${BUILD_NUMBER} .'
            withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                sh 'docker push houdaoufares620/task-manager:v${BUILD_NUMBER}'
            }
        }
        }
        }
        
        stage('Deploy to Kubernetes...'){
            steps{
                echo 'Deploying to Kubernetes..'
                script{
                    sh 'echo "kubectl apply -f k8s/deployment.yml"'
                    sh 'echo "kubectl apply -f k8s/service.yml"'
                    sh 'echo "kubectl set imagedeployment/task-manager-deployment task-manager-container=houdaoufares620/task-manager:v${BUILD_NUMBER} --record"'
                }
            }
        }

    }
}