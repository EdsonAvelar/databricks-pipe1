pipeline {
  agent any

  environment {
    CONDA = "/home/adriano/anaconda3/condabin/conda"
    CONDAENV = "databricks"
    DBURL = "https://adb-6840195589605290.10.azuredatabricks.net"
    DBTOKEN = "dapi0d85b117bfedd50a37a58816eef0438e-3"
    CLUSTERID = "1228-220746-bqqkddxs"
    DATABRICKS = "/home/adriano/anaconda3/bin/databricks"
  }

  stages {

      stage('Begin') {
        steps {
            sh '''#!/usr/bin/env bash
            echo "Inicianddo os trabalhos"      
            $CONDA info      
            pip install -U databricks-cli
            '''
        }
    }

    stage('Execute Notebook') {
        steps {
            sh '''#!/usr/bin/env bash
            echo "Inicianddo os trabalhos"      
            $CONDA info

            ${CONDA} activate ${CONDAENV}      
            pip install -U databricks-cli
            '''
        }
    }

    stage('Setup Databricks') {
        steps {
            withCredentials([string(credentialsId: DBTOKEN, variable: 'TOKEN')]) {
            sh """#!/bin/bash
                # Configure Conda environment for deployment & testing
                ${CONDA} activate ${CONDAENV}

                # Configure Databricks CLI for deployment
                echo "${DBURL} $TOKEN" | databricks configure --token

                # Configure Databricks Connect for testing
                echo "${DBURL} $TOKEN ${CLUSTERID} 0 15001" | databricks-connect configure
                """
            }
        }
    }
  }
}