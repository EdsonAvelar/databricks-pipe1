pipeline {
  stage('setup miniconda') {
    steps {
        sh '''#!/usr/bin/env bash
        wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
        bash miniconda.sh -b -p $WORKSPACE/miniconda
        hash -r
        conda config --set always_yes yes --set changeps1 no
        conda update -q conda

        # Useful for debugging any issues with conda
        conda info -a
        conda config --add channels defaults
        conda config --add channels conda-forge
        conda config --add channels bioconda

        # create snakemake-workflows env
        conda init bash
        conda env create -f envs/snakemake-workflows.yaml
        '''
    }
  }

    stage('Test downloading') {
        steps {
            sh '''#!/usr/bin/env bash
            source $WORKSPACE/miniconda/etc/profile.d/conda.sh
            conda activate miniconda/envs/snakemake-workflows/
            snakemake -s workflows/download_fastq/Snakefile --directory workflows/download_fastq -n -j 48 --quiet
            '''
        }
    }
}