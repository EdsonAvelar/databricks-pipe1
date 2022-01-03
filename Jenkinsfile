pipeline {
  agent any

  environment {
    
    WORKSPACE = '.'
    DBRKS_BEARER_TOKEN = "xyz"
    DBTOKEN="DBTOKEN"
    CLUSTERID="1228-220746-bqqkddxs"
    DBURL="https://adb-6840195589605290.10.azuredatabricks.net"

    TESTRESULTPATH="./teste_results"
    LIBRARYPATH     = "./Libraries"
    OUTFILEPATH     = "./Validation/Output"
    NOTEBOOKPATH = "./Notebooks"
    WORKSPACEPATH   = "/Shared"

  }

  stages {
    stage('Install Miniconda') {
        steps {

            sh '''#!/usr/bin/env bash
            echo "Inicianddo os trabalhos"  
            wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -nv -O miniconda.sh

            rm -r $WORKSPACE/miniconda
            bash miniconda.sh -b -p $WORKSPACE/miniconda
            
            export PATH="$WORKSPACE/miniconda/bin:$PATH"
            
            echo $PATH

            conda config --set always_yes yes --set changeps1 no
            conda update -q conda
            conda create --name mlops2

            '''
        }

    }

    stage('Install Requirements') {
        steps {
            sh '''#!/usr/bin/env bash
            echo "Installing Requirements"  
            source $WORKSPACE/miniconda/etc/profile.d/conda.sh
            conda activate mlops2

            export PATH="$HOME/.local/bin:$PATH"
            echo $PATH

            pip install --user databricks-cli
            pip install -U databricks-connect
            pip install pytest
            databricks --version

           '''
        }

    }
    
      stage('Configure Databricks') {
        steps {
           withCredentials([string(credentialsId: DBTOKEN, variable: 'TOKEN')]) { 
            sh """#!/bin/bash
                
                source $WORKSPACE/miniconda/etc/profile.d/conda.sh
                conda activate mlops2

                #pip install -r requirements.txt
                export PATH="$HOME/.local/bin:$PATH"
                echo $PATH
          
                # Configure Databricks CLI for deployment
                echo "${DBURL}
                $TOKEN" | databricks configure --token

                # Configure Databricks Connect for testing
                echo "${DBURL}
                $TOKEN
                ${CLUSTERID}
                0
                15001" | databricks-connect configure
                  """
           }
      }
    }

   
    stage('Run Unit Tests') {
      steps {

        script {
            try {
              sh """#!/bin/bash
                source $WORKSPACE/miniconda/etc/profile.d/conda.sh
                conda activate mlops2

                # Python tests for libs
                python -m pytest --junit-xml=${TESTRESULTPATH}/TEST-libout.xml ${LIBRARYPATH}/python/dbxdemo/test*.py || true
                """
          } catch(err) {
            step([$class: 'JUnitResultArchiver', testResults: '--junit-xml=${TESTRESULTPATH}/TEST-*.xml'])
            if (currentBuild.result == 'UNSTABLE')
              currentBuild.result = 'FAILURE'
            throw err
          }
        }
      }
    }

    stage('Execute Notebook') {
      steps {
           withCredentials([string(credentialsId: DBTOKEN, variable: 'TOKEN')]) { 
            sh """#!/bin/bash
                
                source $WORKSPACE/miniconda/etc/profile.d/conda.sh
                conda activate mlops2

                #pip install -r requirements.txt
                export PATH="$HOME/.local/bin:$PATH"
                echo $PATH

                # Configure Databricks CLI for deployment
                echo "${DBURL}
                $TOKEN" | databricks configure --token

                # Configure Databricks Connect for testing
                echo "${DBURL}
                $TOKEN
                ${CLUSTERID}
                0
                15001" | databricks-connect configure

                python executenotebook.py --workspace=${DBURL}\
                      --token=$TOKEN\
                      --clusterid=${CLUSTERID}\
                      --localpath=${NOTEBOOKPATH}\
                      --workspacepath=${WORKSPACEPATH}\
                      --outfilepath=${OUTFILEPATH}
                """
           }
      }
    }


    
  } 
}