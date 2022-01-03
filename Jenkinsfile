pipeline {
  agent any

  environment {
    CONDA = "/home/adriano/anaconda3/condabin/conda"
    WORKSPACE = '.'
    DBRKS_BEARER_TOKEN = "xyz"
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
            conda create --name mlops

            '''
        }

    }

    stage('Activate Enviroment') {
          steps {
            sh '''#!/usr/bin/env bash
            source $WORKSPACE/miniconda/etc/profile.d/conda.sh
            conda activate miniconda/envs/mlops/

            DBRKS_BEARER_TOKEN = $DBRKS_BEARER_TOKEN
            export DBRKS_BEARER_TOKEN

            python pipelineScripts/create_cluster.py 
            '''
          }
    }
  }
}