pipeline {
  agent any

  environment {
    CONDA = "/home/adriano/anaconda3/condabin/conda"
    WORKSPACE = '.'
    DBRKS_BEARER_TOKEN = "xyz"
    DBTOKEN="DBTOKEN"
  }

  stages {
     stage('Install Miniconda') {
        steps {
           withCredentials([string(credentialsId: DBTOKEN, variable: 'TOKEN')]) { 
            sh """#!/bin/bash
                # Configure Conda environment for deployment & testing

                echo $TOKEN
                
                source ${CONDAPATH}/bin/activate ${CONDAENV}

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