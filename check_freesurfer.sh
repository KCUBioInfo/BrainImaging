#!/bin/bash

#Script for checking whether Freesurfer successfully completed for all subjects.
#Works by checking whether folders in ouput directory contain at least 200MB of output
#Options for saving a list of files or deleting those directories are commented out but can be used as needed.



mapfile -t my_array < <( du -h -d 1 ../derivatives/Freesurfer )


count=0
for value in "${my_array[@]}"
do
  #echo $value
  parts=( $value )
 
  
  if [ ${parts[0]: -1} == "M" ];
  then
      #echo ${parts[0]: -1}
      #echo ${parts[0]%?}
      if [ ${parts[0]%?} -lt 200 ];
      then
           echo ${parts[1]}
           #echo ${parts[1]} >> ../derivatives/Freesurfer/missed_fs_$(date +'%m-%d-%Y').txt #Save list to file
           count=$(( count + 1 )) #Count how many did not complete
           #rm -rf ${parts[1]} #Remove directories that are too small
      fi
  fi

done

echo $count