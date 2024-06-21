import os
import pandas as pd

def setup_directories(output_dir):
    try:
        # Check for output directory if not exist, we will create it
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        return output_dir
    except Exception as e:
        print(f"Error setting up directories: {e}")
        raise

output_dir = '/in-source-folder'

setup_directories(input_dir, output_dir)
