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

        stage('Generate markdown from applications metadata') {
            steps {
                iterateOverProjects()
                sh 'git status --porcelain=v1'
            }
        }

        stage('Generate and publish Pelican site to Github Pages') {
            when {
                anyOf {
                    branch 'pelican'
                }
            }
            steps {
                withCredentials([string(
                        credentialsId: "indigobot-github-token",
                        variable: "GITHUB_TOKEN")]) {
                    sh 'git fetch origin master:master -f'
                    sh 'git remote set-url origin "https://indigobot:${GITHUB_TOKEN}@github.com/deephdc/deephdc.github.io"'
                    sh 'make github'
                }
            }
        }
    }
}

void iterateOverProjects() {
    data = readYaml (file: 'project_apps.yml')
    data.each {
        repo_name = sh(returnStdout: true, script: "basename ${it.module}")
        repo_name = repo_name.trim()
        repo_dir = "/tmp/${repo_name}"
                            
        script {
            try {
                stage("Application: ${repo_name}") {
                    checkout([  
                        $class: 'GitSCM', 
                        branches: [[name: "refs/heads/master"]], 
                        doGenerateSubmoduleConfigurations: false, 
                        extensions: [[
                            $class: 'RelativeTargetDirectory',
                            relativeTargetDir: repo_dir
                        ]],
                        submoduleCfg: [], 
                        userRemoteConfigs: [[url: it.module]],
                    ])
                    dir(repo_dir) {
                        // TEST: Validate metadata according to DEEP schema
                        sh 'deep-app-schema-validator metadata.json'
                        // TEST: Search for non-ascii characters
                        sh 'python -c "open(\'metadata.json\').read().encode(\'ascii\')"'
                
                        // Generate markdown file from metadata
                        def markdown_file = [repo_name, 'md'].join('.').toLowerCase()
                        sh "${WORKSPACE}/deephdc.github.io/metadata2md.py metadata.json --output-file ${WORKSPACE}/deephdc.github.io/content/modules/${markdown_file}"
                    }
                }
            }
            catch(e) {
                // Continue even if it fails
                env.pipeline_status = 'UNSTABLE'
                currentBuild.result = 'SUCCESS'
            }
        }
    }
}
