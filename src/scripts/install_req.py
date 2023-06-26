import configparser
import os

# This file is gonna be run from Main.py
file = 'install_req.py'
cfg_path = os.getcwd().replace('src', 'config.cfg')
config = configparser.ConfigParser()
config.read(cfg_path)

cout = config.get('Setup', 'cout')
req_path = config.get('Python', 'requirements')

def install_req():
    os.system(f"pip install -r {req_path}")
    if cout : print(f"{file} > Download completed, check logs for errors and warnings.")
