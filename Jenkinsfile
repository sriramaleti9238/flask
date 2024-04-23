pipeline {
    environment {
        IMAGE = "sriramaleti9238/pyth"
        registryCredential = 'dockerhub' // This should match the ID of the Docker Hub credentials in Jenkins
        dockerImage = ''
    }
    agent any 
    stages {
        stage('checkout') {
            steps {
                git branch: 'master',
                url: 'https://github.com/sriramaleti9238/flask'
            }
        }

        stage('Build') {
            steps {
                script {
                    dockerImage = docker.build "${IMAGE}:latest"
                }
            }
        }
        stage('Test Docker') {
            steps {
                script {
                    sh 'docker --version'
                }
            }
        }

        stage('Push image to docker hub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', registryCredential) {
                        dockerImage.push()
                    }
                }
            }
        }
        // stage('Test Docker') {
        //     steps {
        //         script {
        //             sh 'docker --version'
        //         }
        //     }
        // }

        stage('run the docker container') {
            steps {
                script {
                    sh 'docker run -d -p 3000:8083 --name demo-app ${dockerImage}:latest'
                }
            }
        } 
    }
}
