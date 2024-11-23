from build_llvm import *

def build_test_project():
    assert CLANG_CXX_COMPILER.exists()
    shutil.rmtree(TEST_PROJECT_BUILD_DIR, ignore_errors=True)
    cxx_flags = ' '.join(['-static', '-stdlib=libc++'])
    linker_flags = ' '.join(['-lc++abi'])
    command(
        'cmake',
        *('-G', 'Ninja'),
        *('-S', TEST_PROJECT_SRC_DIR),
        *('-B', TEST_PROJECT_BUILD_DIR),
        f'-DCMAKE_BUILD_TYPE:STRING=Release',
        f"-DCMAKE_EXPORT_COMPILE_COMMANDS:BOOL=ON",
        f"-DCMAKE_C_COMPILER:FILEPATH={CLANG_C_COMPILER}",
        f"-DCMAKE_CXX_COMPILER:FILEPATH={CLANG_CXX_COMPILER}",
        f"-DCMAKE_CXX_FLAGS:STRING={cxx_flags}",
        f"-DCMAKE_EXE_LINKER_FLAGS:STRING={linker_flags}"
    )

if __name__ == '__main__':
    build_test_project()
