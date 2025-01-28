import build_llvm
import generate_utilities
import build_test_project

def run_all():
    build_llvm.install_llvm()
    generate_utilities.generate_utilities()
    build_test_project.build_test_project()

if __name__ == '__main__':
    run_all()
