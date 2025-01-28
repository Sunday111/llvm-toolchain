from script_common import *
import run_all

def rerun_all():
    subprocess.check_call(['git', 'clean', '-fdX'], cwd=SCRIPT_DIR)
    run_all.run_all()

if __name__ == '__main__':
    run_all()
