pipeline { 
    environment {
        IMAGE = "shasank2002/pyt"
        dockerImage = ''
    }
    agent any 
    stages {
        stage('checkout') {
                steps {
                git branch: 'master',
                url: 'https://github.com/alpaaprthishasank/flask-doc.git'
                }
        }
        stage('Build') {
            steps {
                script {
                    dockerImage = docker.build "${IMAGE}:latest"
                }
            }
        }

        stage('Push image to docker hub') {
            steps {
                    script {
                        dockerImage.push() 
                     }
                }
            }
        }

        stage('run the docker container') {
            steps {
                sh 'docker run -d -p 80:80 --name demo-app ${IMAGE}:latest'
            }
        
        } 
    }
}