#!/bin/bash

search_dir=$1

echo "Finding .nii.gz files in ${search_dir}"



echo $(ls $search_dir)
filename=$(basename $search_dir)
echo $filename
parent=$(dirname $search_dir)
echo $parent
#find $search_dir -type f -name *.nii > ${parent}/${filename}.txt
find $search_dir -type f -name *_T1w.nii.gz > ${parent}/${filename}_T1w.txt
find $search_dir -type f -name *_T2w.nii.gz > ${parent}/${filename}_T2w.txt
find $search_dir -type f -name *task-rest_*_bold.nii.gz > ${parent}/${filename}_rest.txt
find $search_dir -type f -name *_dwi.nii.gz > ${parent}/${filename}_dwi.txt
cp $search_dir/ndar_subject01.txt ${parent}/${filename}_subjects.tsv