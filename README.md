## END TO END DEFAULT CREDIT CARD ML PROJECT ##

## Create Environement
    conda create -p env python=3.8
    conda activate env
## Create requirement.txt file
    To install all the necessary liabaries
    pip install -r requirement.txt
## Create setup.py file
    use of setup.py - To make the folder into packages
    run-python setup.py install
## Create SRC folder 
    Entire project life cycle will run in this folder
    Create __init__.py in each folder to use as package.
        create logger.py
        create exception.py

## Project Life Cycle
    1. Data Collection
    2.EDA
    3.Feature Engerning
    4.Model Training
    5.Model Evaluation
    6.Model Deployment
## Create Component folder insise src
    Inside it
    1.__init__.py
    2.data_injestion.py
    3.data.transsformation.py
## Create pipline folder inside src
    1.__init__.py
    2.training_pipeline.py
    3gi.prediction_pipline.py
## create a new repository on the command line

git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Ksanu275/Interview_DS.git
git push -u origin main

## push an existing repository from the command line
git remote add origin https://github.com/Ksanu275/Interview_DS.git
git branch -M main
git push -u origin main
