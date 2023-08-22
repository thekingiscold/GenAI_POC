pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = 'your_aws_access_key'
        AWS_SECRET_ACCESS_KEY = 'your_aws_secret_key'
        EC2_INSTANCE_IP = 'your_ec2_instance_ip'
        GIT_USERNAME = 'your_git_username'
        GIT_PASSWORD = 'your_git_password_or_personal_access_token'
        REPO_URL = 'https://github.com/username/projectname.git'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout([$class: 'GitSCM', 
                              branches: [[name: '*/master']],
                              userRemoteConfigs: [[url: "${env.REPO_URL}", credentialsId: 'your_git_credentials_id']]])
                }
            }
        }

        stage('Build') {
            steps {
                sh 'npm install'
                sh 'npm run build'
            }
        }

        stage('Deploy') {
            steps {
                sh "ssh ubuntu@${env.EC2_INSTANCE_IP} 'mkdir -p /path/to/your/deployment/folder'"
                sh "scp -r build/* ubuntu@${env.EC2_INSTANCE_IP}:/path/to/your/deployment/folder/"
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed'
        }
    }
}
