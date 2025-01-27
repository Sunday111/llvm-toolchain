from script_common import *


def generate_cmake_toolchain_file():
    file_content = f"""cmake_minimum_required(VERSION 3.16)
set(CMAKE_C_COMPILER {CLANG_C_COMPILER} CACHE STRING "")
set(CMAKE_CXX_COMPILER {CLANG_CXX_COMPILER} CACHE STRING "")
set(CMAKE_LINKER {LLVM_LINKER_PATH} CACHE STRING "")
set(CMAKE_AR {LLVM_AR_PATH} CACHE STRING "")
set(CMAKE_RANLIB {LLVM_RANLIB_PATH} CACHE STRING "")
set(CMAKE_CXX_FLAGS "{TOOLCHAIN_CXX_FLAGS}" CACHE STRING "")
set(CMAKE_EXE_LINKER_FLAGS "{TOOLCHAIN_LINKER_FLAGS}" CACHE STRING "")
"""

    with open(file=CMAKE_TOOLCHAIN_FILEPATH, mode="wt", encoding="utf-8") as file:
        file.write(file_content)


def generate_vscode_settings():
    patch_json(
        VSCODE_SETTINGS_JSON,
        {
            "clangd.path": CLANGD_PATH.as_posix(),
            "clang-format.executable": CLANGFORMAT_PATH.as_posix(),
        },
    )


def generate_vscode_cmake_kits_json():
    write_json(
        VSCODE_CMAKE_KITS_JSON,
        [
            {
                "name": f"LLVM from sources, {LLVM_GIT_TAG}",
                "compilers": {
                    "c": CLANG_C_COMPILER.as_posix(),
                    "cxx": CLANG_CXX_COMPILER.as_posix(),
                },
                "toolchainFile": CMAKE_TOOLCHAIN_FILEPATH.as_posix(),
            }
        ],
    )


def generate_utilities():
    shutil.rmtree(GENERATED_DIR, ignore_errors=True)
    GENERATED_DIR.mkdir(exist_ok=True)
    generate_cmake_toolchain_file()
    shutil.copytree(src=VSCODE_TEMPLATE_DIR, dst=VSCODE_GEN_PATH)
    generate_vscode_settings()
    generate_vscode_cmake_kits_json()


if __name__ == "__main__":
    generate_utilities()
