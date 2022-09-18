import os
from site import abs_paths
abs_path=os.path.abspath(__file__)
base_dir=os.path.dirname(abs_path)
vdo_dir=os.path.join(base_dir,'data')
sample_dir=os.path.join(vdo_dir,'samples')
sample_input=os.path.join(sample_dir,'input')
sample_output=os.path.join(sample_dir,'output')