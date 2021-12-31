pipeline {
  agent any

  environment {
    CONDA = "/home/adriano/anaconda3/condabin/conda"
  }

  stages {

      stage('Begin') {
        steps {
            sh '''#!/usr/bin/env bash
            echo "Inicianddo os trabalhos"  
            mkdir -p venv_dir
            python -m venv venv_dir
            
            . ./venv_dir/bin/activate
            pip install -r requirements.txt
           
            '''
        }
    }

  }
}