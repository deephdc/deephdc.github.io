#!/usr/bin/groovy

@Library(['github.com/indigo-dc/jenkins-pipeline-library']) _

pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile.build'
        }
    }

    stages {
        stage('Fetch repository') {
            steps {
                checkout scm
            }
        }

        stage('Generate Pelican site') {
            when {
                not { branch 'master' }
                not { branch 'pelican' }
            }
            steps {
                sh 'make html'
            }
        }

        stage('Generate and publish Pelican site to Github Pages') {
            when {
                anyOf {
                    branch 'pelican'
                    branch 'add_jenkinsfile'
                }
            }
            steps {
                sh 'make html'
                sh 'git config user.name "indigobot"'
                sh 'git config user.email "orviz@cern.ch"'
                sh 'git fetch origin master:master'
                sh 'make github'
            }
        }
    }
}
