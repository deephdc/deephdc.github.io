#!/usr/bin/groovy

@Library(['github.com/indigo-dc/jenkins-pipeline-library@1.4.0']) _

pipeline {
    agent {
        label 'deep-oc'
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

        stage('Update submodules @deep-oc') {
            when {
                allOf {
                    branch 'pelican'
                    not { triggeredBy 'UpstreamCause' }
                }
            }
            steps {
                // Get last version of DEEP-OC modules 
                JenkinsBuildJob(
                    "Pipeline-as-code/deep-oc/master",
                    [booleanParam(name: 'disable_oc_build', value: true)])
            }
        }

        stage('Generate markdown from applications metadata') {
            when {
                branch 'pelican'
            }
            steps {

                iterateOverProjects()
                sh 'git status --porcelain=v1'
                sh 'git diff --diff-filter=M'
            }
        }
	
        stage('Generate and publish Pelican site to Github Pages') {
            when {
                branch 'pelican'
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
    subdir_name = 'deep-oc-subdir'

    checkout([
        $class: 'GitSCM',
        branches: [[name: '*/master']],
        doGenerateSubmoduleConfigurations: false,
        extensions: [
            [
                $class: 'RelativeTargetDirectory',
                relativeTargetDir: "$subdir_name"
            ],
            [
                $class: 'SubmoduleOption',
                disableSubmodules: false,
                parentCredentials: false,
                recursiveSubmodules: true,
                reference: '',
                trackingSubmodules: false,
            ]
        ],
        submoduleCfg: [],
        userRemoteConfigs: [[url: 'https://github.com/deephdc/deep-oc']]]
    )
	
    dir(subdir_name) { 
        any_build_failure = false
        data = sh(
            script: 'git submodule | awk \'{print $2}\'',
            returnStdout: true
        ).trim().split()
        data.each{
            repo_name = sh(returnStdout: true, script: "basename ${it}").trim()
            dir(repo_name) {
                try {
                    // TEST: Validate metadata according to DEEP schema
                    sh 'deep-app-schema-validator metadata.json'
                    // TEST: Search for non-ascii characters
                    sh 'python -c "open(\'metadata.json\').read().encode(\'utf8\')"'
                    // Generate markdown file from metadata
                    def markdown_file = [repo_name, 'md'].join('.').toLowerCase()
                    sh "${WORKSPACE}/metadata2md.py metadata.json --output-file ${WORKSPACE}/content/modules/${markdown_file}"
                }
                catch (e) {
                    echo "An error occurred while building DEEP module <${repo_name}>"
                    any_build_failure = true
                }
            }
        }
    }
    
    if (any_build_failure) {
        echo "There were errors building DEEP modules. Setting the build status as UNSTABLE"
        currentBuild.result = 'UNSTABLE'
    }
}
