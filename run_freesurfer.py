# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 10:54:52 2023

@author: JShaffer
"""

import os
import subprocess
import pandas as pd


HOST_DATA_PATH="C:\\Users\\JShaffer.KCUMB\\Documents\\Research\\test_data"
SUBJECTS_DIR="/derivatives/FreeSurfer"
CONTAINER_DATA_PATH="/data"
CONTAINER_NAME_PREFIX="freesurfer"
N_CONTAINERS=1
IMAGE_NAME="freesurfer"

#Create Docker Containers 
for i in range(N_CONTAINERS):

    #e.g. docker run -i -v C:\Users\JShaffer.KCUMB\Documents\dev\BrainImaging:/test_data --name ubuntu_1 ubuntu
    command_string = f"docker run -d -i -v {HOST_DATA_PATH}:{CONTAINER_DATA_PATH} -e SUBJECTS_DIR={CONTAINER_DATA_PATH}{SUBJECTS_DIR} --name {CONTAINER_NAME_PREFIX}_{str(i)} {IMAGE_NAME}"
    #command_string = "docker run -i -v " + HOST_DATA_PATH + ":" + CONTAINER_DATA_PATH + " --name " + CONTAINER_NAME_PREFIX + "_" + str(i) + " " + IMAGE_NAME
    print(command_string)
    subprocess.run(command_string)
    
    
    subj_id = 'sub-01'
    #Configure FreeSurfer Subject Directory
    command_string = f"docker exec {CONTAINER_NAME_PREFIX}_{str(i)} recon-all -all -subject {subj_id} -i {CONTAINER_DATA_PATH}/{subj_id}/anat/{subj_id}_T1w.nii.gz"
    print(command_string)    
    p = subprocess.run(command_string, capture_output = True)
    
    print(p)
    #result = subprocess.run(f"docker exec -it {CONTAINER_NAME_PREFIX}_{str(i)} echo $SUBJECTS_DIR", capture_output=True)
    
    #print(result)





#Read in subject list


#Split list between containers


#Run Freesurfer on list








#Stop and Delete Docker Containers
#for i in range(N_CONTAINERS):
    
#    command_string = f"docker stop {CONTAINER_NAME_PREFIX}_{str(i)}"
#    print(command_string)    
#    subprocess.run(command_string)

    
#    command_string = f"docker rm {CONTAINER_NAME_PREFIX}_{str(i)}"
#    print(command_string)    
#    subprocess.run(command_string)
