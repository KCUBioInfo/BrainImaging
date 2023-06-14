import os
import subprocess

# Paths to input and output directories
input_dir = '/data/input'
output_dir = '/data/output'

# Get the input NIfTI file
input_file = os.path.join(input_dir, 'input_brain.nii.gz')

# Perform brain parcellation using Freesurfer
freesurfer_cmd = f'recon-all -i {input_file} -s output_subject -all'
subprocess.run(freesurfer_cmd, shell=True)

# Move the output files to the output directory
subject_dir = os.path.join('output_subject')
output_files = [
    'aparc+aseg.mgz',
    'aparc.a2009s+aseg.mgz',
    # Add more output files as needed
]

for file in output_files:
    file_path = os.path.join(subject_dir, 'mri', file)
    output_path = os.path.join(output_dir, file)
    subprocess.run(['mv', file_path, output_path])

# Print a success message
print('Brain parcellation completed!')