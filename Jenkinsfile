pipeline {

    agent any


    parameters {

        booleanParam(
            name: 'RUN_SECURITY_CHECK',
            defaultValue: false,
            description: 'Run the additional security validation stage'
        )
    }


    stages {


        stage('Checkout') {

            steps {

                echo '=============================================='
                echo 'CHECKOUT STAGE'
                echo '=============================================='

                echo 'Checking out source code from GitHub...'

                git branch: 'main',
                    url: 'https://github.com/DharukDharshan-10/Jenkins-Project-4.git'

                echo 'Source code checkout completed.'
            }
        }


        stage('Application Validation') {

            steps {

                echo '=============================================='
                echo 'APPLICATION VALIDATION STAGE'
                echo '=============================================='

                echo 'Starting application validation...'

                bat '"C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" app.py'

                echo 'Application validation completed.'
            }
        }


        stage('Security Validation') {

            when {

                expression {

                    return params.RUN_SECURITY_CHECK == true
                }
            }


            steps {

                echo '=============================================='
                echo 'SECURITY VALIDATION STAGE'
                echo '=============================================='

                echo 'RUN_SECURITY_CHECK is TRUE.'

                echo 'Starting additional security validation...'

                bat '"C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" security_check.py'

                echo 'Security validation completed.'
            }
        }


        stage('Build Summary') {

            steps {

                echo '=============================================='
                echo 'BUILD SUMMARY'
                echo '=============================================='

                echo 'Application validation completed successfully.'

                script {

                    if (params.RUN_SECURITY_CHECK) {

                        echo 'Security Validation : EXECUTED'

                    } else {

                        echo 'Security Validation : SKIPPED'
                    }
                }

                echo 'Pipeline execution completed.'
            }
        }
    }


    post {

        success {

            echo '=============================================='
            echo 'PIPELINE STATUS: SUCCESS'
            echo '=============================================='
        }


        failure {

            echo '=============================================='
            echo 'PIPELINE STATUS: FAILURE'
            echo '=============================================='
        }


        always {

            echo 'Jenkins pipeline execution has finished.'
        }
    }
}
