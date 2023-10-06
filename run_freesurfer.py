# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 10:54:52 2023

@author: JShaffer
"""

import os
import subprocess
import pandas as pd


def create_container(container_name, image_name, host_path='', container_path='', subjects_dir='', self_terminate = True):
    #Create Docker Container

    #e.g. docker run -i -v C:\Users\JShaffer.KCUMB\Documents\dev\BrainImaging:/test_data --name ubuntu_1 ubuntu
    command_string = f"docker run -d -i -v {host_path}:{container_path} -e SUBJECTS_DIR={subjects_dir} --name {container_name} {image_name}"
    #command_string = "docker run -i -v " + HOST_DATA_PATH + ":" + CONTAINER_DATA_PATH + " --name " + CONTAINER_NAME_PREFIX + "_" + str(i) + " " + IMAGE_NAME
    print(command_string)
    subprocess.run(command_string)
    
    
        
def run_subject(subj_id, container_name, t1_path, t2_path = ''):
   
    #Configure FreeSurfer Subject Directory

    #If T2 file is available, run with T2 file
    if t2_path != '':
        command_string = f"docker exec -d {container_name} recon-all -all -subject {subj_id} -i {t1_path} -T2 {t2_path} -T2pial"
    else:
        command_string = f"docker exec -d {container_name} recon-all -all -subject {subj_id} -i {t1_path}"
    print(command_string)    
    p = subprocess.run(command_string, capture_output = True, universal_newlines=True)
    #print(p)
    
    #with open(subj_id + '_stdout.txt', 'w') as f:
    #    f.write(p.stdout)
    #with open(subj_id + '_stderr.txt', 'w') as f:
    #    f.write(p.stderr)
    
    #return p
    
def delete_container(container_name):
    #Stop and Delete Docker Container
        
    command_string = f"docker stop {container_name}"
    print(command_string)    
    subprocess.run(command_string)

    
    command_string = f"docker rm {container_name}"
    print(command_string)    
    subprocess.run(command_string)    
    
#Define Constants
#HOST_DATA_PATH="C:\\Users\\JShaffer.KCUMB\\Documents\\Research\\test_data" #Path to shared directory on host machine
HOST_DATA_PATH="D:\\" #Path to shared directory on host machine - lab desktops

SUBJECTS_DIR="/data/derivatives/Freesurfer" #Must be full path to data within container
CONTAINER_DATA_PATH="/data"     #Path to place share relative to within container
CONTAINER_NAME_PREFIX="freesurfer"
N_CONTAINERS=160
START_INDEX=80
#START_INDEX=160
IMAGE_NAME="freesurfer"
    
#Script
#df = pd.read_excel("C:\\Users\\JShaffer.KCUMB\\Documents\\Research\\test_data\\participant_paths.xlsx")
df = pd.read_excel('D:\\BD_NDA\\1218563_participant_image_paths.xlsx')

for i,v in enumerate(df.index[START_INDEX:START_INDEX + N_CONTAINERS]):
    
    subj_id = df.loc[v, 'subj_id'] + "_" + df.loc[v, 'session']
    t1_path = CONTAINER_DATA_PATH + df.loc[v, 't1w']
    t2_path = CONTAINER_DATA_PATH + df.loc[v, 't2w']
    
    
    print(subj_id)
    print(t1_path)
    print(t2_path)

    #Start Container
    create_container('FS_'+ str(i), IMAGE_NAME, HOST_DATA_PATH, CONTAINER_DATA_PATH, SUBJECTS_DIR)

    output = run_subject(subj_id, 'FS_'+ str(i), t1_path, t2_path = '')






