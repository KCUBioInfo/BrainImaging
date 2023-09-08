#!/bin/bash

#Build the docker image from the dockerfile
#docker build -t freesurfer .


#On Windows, execute this in Powershell to create a container
#docker run -i -v C:\Users\JShaffer.KCUMB\Documents\dev\BrainImaging:/data --name ubuntu_1 ubuntu

#Next set the SUBJECTS_DIR to the folder where you want to save FreeSurfer Output - this is likely the mounted directory
#export SUBJECTS_DIR=/data/derivatives/FreeSurfer