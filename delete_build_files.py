from script_common import *

def delete_build_files():
    shutil.rmtree(LLVM_BUILD_DIR, ignore_errors=True)
    shutil.rmtree(TEST_PROJECT_BUILD_DIR, ignore_errors=True)

if __name__ == '__main__':
    delete_build_files()
