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
                }
            }
            steps {
                withCredentials([string(credentialsId: "indigobot-github-token",
                                 variable: "GITHUB_TOKEN")]) {
                    sh 'git branch -D master'
                    sh 'git fetch origin master:master'
                    sh 'git remote set-url origin "https://indigobot:${GITHUB_TOKEN}@github.com/deephdc/deephdc.github.io"'
                    sh 'make github'
                }
            }
        }
    }
}
