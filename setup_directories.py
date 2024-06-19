import os
import pandas as pd

def setup_directories(output_dir):
    # Check if output dir exists else create
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

output_dir = '/ready-for-processing'

setup_directories(output_dir)
