from script_common import *

def build_test_project():
    assert CLANG_CXX_COMPILER.exists()
    shutil.rmtree(TEST_PROJECT_BUILD_DIR, ignore_errors=True)
    command(
        'cmake',
        *('-G', 'Ninja'),
        *('-S', TEST_PROJECT_SRC_DIR),
        *('-B', TEST_PROJECT_BUILD_DIR),
        f'-DCMAKE_TOOLCHAIN_FILE:FILEPATH={CMAKE_TOOLCHAIN_FILEPATH}',
        f'-DCMAKE_BUILD_TYPE:STRING=Release',
        f"-DCMAKE_EXPORT_COMPILE_COMMANDS:BOOL=ON",
    )
    command('cmake', '--build', TEST_PROJECT_BUILD_DIR)
    command(TEST_PROJECT_BUILD_DIR / 'test_project')

if __name__ == '__main__':
    build_test_project()
