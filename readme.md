# Build llvm toolchain and libc++

## `script_common.py`
Helper file with settings and utilities used by other scripts.

## `build_llvm.py`

- Does a shallow clone of [llvm-project](https://github.com/llvm/llvm-project). By default it clones main branch. Change `LLVM_GIT_TAG` variable in settings if you need that.
- Generates build files to `build-llvm` directory.
- Installs llvm to `llvm-install` directory.

## `generate_utilities.py`

Generates some useful files to use built toolchain easily.

### `generated/llvm-toolchain.cmake`

Toolchain file for CMake. This toolchain specifies paths to clang, clang++ and some compile options to use libc++ by default.

You can use it in your project this way

```bash
cmake -S path/to/your/project -B path/to/build/directory -DCMAKE_TOOLCHAIN_FILE=path/to/toolchain/file
```

### `generated/.vscode`

Configuration files for VS Code. Just put these files into the root of your workspace and reload window. You might need only a subset of them, it depends on extensions you use.

#### `generated/.vscode/settings.json`

`.vscode` dir can be put into your project root directory or used as an example for your vscode user settings. 

Content:
- path to [cland](https://clangd.llvm.org/), required by [clangd extension](https://marketplace.visualstudio.com/items?itemName=llvm-vs-code-extensions.vscode-clangd)
- path to [clang-format](https://clang.llvm.org/docs/ClangFormat.html), required by [clang-format extension](https://marketplace.visualstudio.com/items?itemName=xaver.clang-format)


#### `generated/.vscode/cmake-kits.json`

Specifies location of LLVM toolchain for [CMake Tools extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools). It allows you to use built toolchain from this extension.

#### `generated/.vscode/launch.json`

Simple launch.json file to debug C++ code using commands and UI from [CMake Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools) and [C/C++](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools) extensions.


## `build_test_project.py`

Builds `test-project` to check that installed toolchain actually works.

## `delete_build_files.py`

Removes build directories for llvm and test project. They are a waste of space if you are not going to build llvm frequently.
