import build_llvm
import generate_utilities
import build_test_project
import delete_build_files

def run_all():
    build_llvm.install_llvm()
    generate_utilities.generate_utilities()
    build_test_project.build_test_project()
    delete_build_files.delete_build_files()

if __name__ == '__main__':
    run_all()
