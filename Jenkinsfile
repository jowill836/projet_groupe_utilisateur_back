pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/jowill836/projet_groupe_utilisateur_back.git']]])
      }
    }

    stage('Build') {
      steps {
        sh 'pipenv install'
      }
    }

    stage('Test') {
      steps {
        sh 'pipenv run python manage.py test'
      }
    }
  }
}
