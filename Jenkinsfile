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
                
                
              """
           }
      }
    }
  } 
}