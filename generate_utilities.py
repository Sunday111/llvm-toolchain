from script_common import *

def generate_cmake_toolchain_file():
    file_content = f'''cmake_minimum_required(VERSION 3.16)
set(CMAKE_C_COMPILER {CLANG_C_COMPILER})
set(CMAKE_CXX_COMPILER {CLANG_CXX_COMPILER})
set(CMAKE_LINKER {LLVM_LINKER_PATH})
set(CMAKE_AR {LLVM_AR_PATH})
set(CMAKE_RANLIB {LLVM_RANLIB_PATH})
set(CMAKE_CXX_FLAGS "{TOOLCHAIN_CXX_FLAGS}")
set(CMAKE_EXE_LINKER_FLAGS "{TOOLCHAIN_LINKER_FLAGS}")
'''

    GENERATED_DIR.mkdir(exist_ok=True)
    with open(file=CMAKE_TOOLCHAIN_FILEPATH, mode='wt', encoding='utf-8') as file:
        file.write(file_content)

def generate_vscode_settings():
    data = dict()
    data['cmake.configureArgs'] = [
        f'-DCMAKE_TOOLCHAIN_FILE:FILEPATH={CMAKE_TOOLCHAIN_FILEPATH}',
    ]
    data['clangd.path'] = CLANGD_PATH.as_posix()
    data['clang-format.executable'] = CLANGFORMAT_PATH.as_posix()

    VSCODE_GEN_PATH.mkdir(exist_ok=True)
    with open(file=VSCODE_SETTINGS_JSON, mode='wt', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def generate_utilities():
    generate_cmake_toolchain_file()
    generate_vscode_settings()

if __name__ == '__main__':
    generate_utilities()
