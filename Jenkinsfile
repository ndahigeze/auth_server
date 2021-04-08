pipeline {
  agent any
   environment {
        PROJECT_NAME = 'bfw_e_commerce_frontend'
        DOCKER_REGISTRY = 'ndahigeze/oauthserver'
        DOCKER_CONTAINER_NAME = 'oauthserver'
        DOCKER_PORT_BINDING = '8090:80'
    }

  stages {
    stage('build and push docker image') {

            steps {
                sh  "docker build . -f Dockerfile -t ${env.DOCKER_REGISTRY}:${env.GIT_COMMIT}"
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