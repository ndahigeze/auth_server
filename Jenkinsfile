pipeline {
   agent any
   environment {
        PROJECT_NAME = 'AUTHSERVER'
        DOCKER_REGISTRY = 'ndahigeze/oauthserver'
        DOCKER_CONTAINER_NAME = 'oauthserver'
        DOCKER_PORT_BINDING = '8090:80'
    }

  stages {
    stage('build and push docker image') {
            steps {
                 sh  "docker build . -f Dockerfile -t ${env.DOCKER_REGISTRY}:${env.GIT_COMMIT}"
                 sh  'cat ~/password.txt | docker login --username ndahigeze --password-stdin'
                 sh "docker push ${env.DOCKER_REGISTRY}:${env.GIT_COMMIT}"
                 cleanWs()
            }
    }
    stage ('Test'){
      steps{
         echo "test"
      }
    }

    stage ('Deploy'){
      steps{

        echo 'Deploying'
      }
    }

  }
}