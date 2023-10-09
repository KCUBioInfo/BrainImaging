# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 13:26:30 2023

@author: jshaffer
"""



import pandas as pd

#package_num = '1218615'
package_num = '1220664'
#package_num = '1218611'


t1_file = 'D:\\BD_NDA\\Package_' + package_num + '_T1w.txt'
t2_file = 'D:\\BD_NDA\\Package_' + package_num + '_T2w.txt'
rest_file = 'D:\\BD_NDA\\Package_' + package_num + '_rest.txt'
dwi_file = 'D:\\BD_NDA\\Package_' + package_num + '_dwi.txt'

df = pd.read_excel('D:\\BD_NDA\\participant_paths3.xlsx')
new_df = pd.DataFrame(columns=['subj_id', 'study_id', 'session', 't1w', 't2w', 'rest', 'dwi'])

#subj_id = df.iloc[0]['ID']
#study_id = df.iloc[0]['src_subject_id']

max_ses = 0

#These indices need to match the index for the study from participant_paths2.xlsx
#for i in df.index[0:228]: #1218563
#for i in df.index[228:325]: #1218615
for i in df.index[7710:7861]: #1220664
#for i in df.index[7710:7711]: #1220745
#for i in df.index[5180:5750]: #1220611
#first index: subtract two from cell number, second index: subtract one

    subj_id = df.iloc[i]['ID']
    #study_id = str(df.iloc[i]['src_subject_id'])
    study_id = '.' + str(df.iloc[i]['src_subject_id'])+'/' #664
    #study_id = '_' + str(df.iloc[i]['src_subject_id'])+'_' #611
    print(study_id)
    t1_paths = []
    with open(t1_file, 'r') as f:
        lines = f.readlines()
        
        for line in lines:
            if line.find(str(study_id)) != -1:
                print(line)
                t1_paths.append(line)
    
    t2_paths = []
    with open(t2_file, 'r') as f:
        lines = f.readlines()
        
        for line in lines:
            if line.find(str(study_id)) != -1:
                #print(line)
                t2_paths.append(line)
                
    rest_paths = []
    with open(rest_file, 'r') as f:
        lines = f.readlines()
        
        for line in lines:
            if line.find(str(study_id)) != -1:
                #print(line)
                rest_paths.append(line)
                
    dwi_paths = []
    with open(dwi_file, 'r') as f:
        lines = f.readlines()
        
        for line in lines:
            if line.find(str(study_id)) != -1:
                #print(line)
                dwi_paths.append(line)
                
    #print(study_id)
    
    """
    sessions = []
    for img in t1_paths:
        tmp = img.split('/')
        tmp2 = tmp[-1].split('_')
        for t in tmp2:
            #if t[0:4] == 'ses-':
            if t[0] == 's':   
                #print(t)
                sessions.append(t[1])

    sub_dict = {'subj_id': subj_id,
                'study_id': study_id,
                'sessions':{}}
    for ses in sessions:
        print(ses)
        
        sub_dict['sessions'][ses] = {'t1w': [j for j in t1_paths if '_s' + str(ses) + '_' in j],
                    't2w': [j for j in t2_paths if '_s' + str(ses) + '_' in j],
                    'rest': [j for j in rest_paths if '_s' + str(ses) + '_' in j],
                    'dwi': [j for j in dwi_paths if '_s' + str(ses) + '_' in j]
                    }
        
        new_df.loc[len(new_df.index)] = [subj_id, study_id, ses, ';'.join([j.strip().replace('/d', '', 1) for j in t1_paths if '_s' + str(ses) + '_' in j]), ';'.join([j.strip().replace('/d', '', 1) for j in t2_paths if '_s' + str(ses) + '_' in j]), 
                                     ';'.join([j.strip().replace('/d', '', 1) for j in rest_paths if '_s' + str(ses) + '_' in j]), ';'.join([j.strip().replace('/d', '', 1) for j in dwi_paths if '_s' + str(ses) + '_' in j])]
   """           
    
    new_df.loc[len(new_df.index)] = [subj_id, study_id, 0, ';'.join([j.strip().replace('/d', '', 1) for j in t1_paths]), ';'.join([j.strip().replace('/d', '', 1) for j in t2_paths]), ';'.join([j.strip().replace('/d', '', 1) for j in rest_paths]), ';'.join([j.strip().replace('/d', '', 1) for j in dwi_paths])]
    
    new_df.to_excel('D:\\BD_NDA\\' + package_num + '_participant_image_paths.xlsx', index=False)
    #print(sub_dict)
    
   