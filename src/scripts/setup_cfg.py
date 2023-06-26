import configparser
import os

config = configparser.ConfigParser()

# This file is gonna be run from Main.py
path = os.getcwd() # Setup
user = os.getlogin()
file = 'setup_cfg.py'
cfg_path = path.replace('src', 'config.cfg')
root_path = path.replace('src', '')
libs = root_path + 'src\libs\\'
cout = True
first_launch = False
requirements = path.replace('src', 'requirements.txt')

try:
    with open(cfg_path):
        pass
except FileNotFoundError: raise FileNotFoundError

version = '3.8' # Python

variables = {'user':user, 'rpath':root_path, 'libs':libs, 'cout':str(cout), 'version':version, 'first_launch':str(first_launch), 'requirements':requirements}

config.read(cfg_path)

config.set('Setup', 'user', user)
config.set('Setup', 'rpath', root_path)
config.set('Setup', 'libs', libs)
config.set('Setup', 'cout', str(cout))

config.set('Python', 'version', version)
config.set('Python', 'requirements', requirements)


def reset_cfg():
    for section in config.sections():

        # Iterate over each variable in the section
        for variable in config.options(section):
            config.set(section, variable, variables[variable])
            if cout : print(f"{file} > Variable {variable} in [{section}] set to default.")
    if cout : print(f"{file} > Cleared {cfg_path} file to it's default settings.")

if config.get('User', 'first_launch') != 'True': os._exit(0)
else: reset_cfg()

def setup_cfg():
    with open(cfg_path, 'w') as configfile:
        config.write(configfile)
        if cout : print(f"{file} > File {cfg_path} successfully set up!")
