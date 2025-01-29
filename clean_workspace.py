from script_common import *

def clean_workspace():
    subprocess.check_call(['git', 'clean', '-fdX'], cwd=SCRIPT_DIR)

if __name__ == '__main__':
    clean_workspace()
