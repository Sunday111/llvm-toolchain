import subprocess
from pathlib import Path
import shutil
import json

SCRIPT_DIR = Path(__file__).parent.resolve()

# Settings
LLVM_SRC_DIR = SCRIPT_DIR / "llvm-project"
LLVM_BUILD_DIR = SCRIPT_DIR / "llvm-build"
LLVM_INSTALL_DIR = SCRIPT_DIR / "llvm-install"
LLVM_GIT_URL = "https://github.com/llvm/llvm-project"
LLVM_GIT_TAG = "main"
TEST_PROJECT_SRC_DIR = SCRIPT_DIR / "test-project"
TEST_PROJECT_BUILD_DIR = SCRIPT_DIR / "test-project-build"
GENERATED_DIR = SCRIPT_DIR / "generated"
CMAKE_TOOLCHAIN_FILEPATH = GENERATED_DIR / "llvm-toolchain.cmake"
VSCODE_GEN_PATH = GENERATED_DIR / ".vscode"
TEMPLATES_DIR = SCRIPT_DIR / "templates"
VSCODE_TEMPLATE_DIR = TEMPLATES_DIR / ".vscode"
TOOLCHAIN_CXX_FLAGS = " ".join(["-static", "-stdlib=libc++"])
TOOLCHAIN_LINKER_FLAGS = " ".join(["-lc++abi"])

# Utilities
LLVM_BIN_DIR = LLVM_INSTALL_DIR / "bin"
CLANG_C_COMPILER = LLVM_BIN_DIR / "clang"
CLANG_CXX_COMPILER = LLVM_BIN_DIR / "clang++"
LLVM_LINKER_PATH = LLVM_BIN_DIR / "ld.lld"
LLVM_AR_PATH = LLVM_BIN_DIR / "llvm-ar"
LLVM_RANLIB_PATH = LLVM_BIN_DIR / "llvm-ranlib"
CLANGD_PATH = LLVM_BIN_DIR / "clangd"
CLANGFORMAT_PATH = LLVM_BIN_DIR / "clang-format"
VSCODE_SETTINGS_JSON = VSCODE_GEN_PATH / "settings.json"
VSCODE_CMAKE_KITS_JSON = VSCODE_GEN_PATH / "cmake-kits.json"


def command(*args):
    subprocess.check_call([*args])


def read_json(path: Path) -> dict:
    with open(file=path, mode="rb") as file:
        return json.load(file)


def write_json(path: Path, data: dict | list):
    with open(file=path, mode="w") as file:
        json.dump(data, file, indent=4)


def patch_json(path: Path, patch: dict):
    data = read_json(path)
    data.update(patch)
    write_json(path, data)
