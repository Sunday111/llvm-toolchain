from script_common import *

def install_llvm():
    if not LLVM_SRC_DIR.exists():
        command(
            'git',
            *('clone', LLVM_GIT_URL),
            *('--depth', '1'),
            *('--branch', LLVM_GIT_TAG),
            LLVM_SRC_DIR
        )

    enabled_projects = 'clang;lld;clang-tools-extra'
    enabled_runtimes = 'libcxx;libcxxabi;libunwind'

    command(
        'cmake',
        *('-G', 'Ninja'),
        *('-S', LLVM_SRC_DIR / 'llvm'),
        *('-B', LLVM_BUILD_DIR),
        f'-DCMAKE_BUILD_TYPE=Release',
        f'-DCMAKE_INSTALL_PREFIX={LLVM_INSTALL_DIR}',
        "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON",
        f'-DLLVM_ENABLE_PROJECTS={enabled_projects}',
        f'-DLLVM_ENABLE_RUNTIMES={enabled_runtimes}',
        "-DCLANG_DEFAULT_LINKER=lld",
        "-DCLANG_DEFAULT_CXX_STDLIB:STRING=libc++",
        "-DLIBCXX_ENABLE_SHARED:BOOL=ON",
        "-DLIBCXX_ENABLE_STATIC:BOOL=ON",
    )

    command(
        'cmake',
        *('--build', LLVM_BUILD_DIR),
        *('--target', 'install')
    )

if __name__ == '__main__':
    install_llvm()
