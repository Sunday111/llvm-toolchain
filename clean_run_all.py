from script_common import *
import clean_workspace
import run_all

def rerun_all():
    clean_workspace.clean_workspace()
    run_all.run_all()

if __name__ == '__main__':
    rerun_all()
