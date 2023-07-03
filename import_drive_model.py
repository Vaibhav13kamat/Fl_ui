# this downloads the model from the drive 
# 


import gdown

file_id = "https://drive.google.com/file/d/16IEmKMjmnClJwEPsZQryV_lM7pjZ1SyC/view?usp=sharing?"
output_file = "model.h5"

gdown.download(file_id, output_file)
