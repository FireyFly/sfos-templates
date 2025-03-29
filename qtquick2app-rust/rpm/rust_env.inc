# https://github.com/sailfishos/gecko-dev/blob/master/rpm/xulrunner-qt5.spec#L283-L287
export SB2_RUST_TARGET_TRIPLE=%{SB2_TARGET}

# https://github.com/sailfishos/gecko-dev/blob/master/rpm/xulrunner-qt5.spec#L300-L305
# This avoids a malloc hang in sb2 gated calls to execvp/dup2/chdir during
# fork/exec. It has no effect outside sb2 so doesn't hurt native builds.
export SB2_RUST_EXECVP_SHIM="/usr/bin/env LD_PRELOAD=/usr/lib/libsb2/libsb2.so.1 /usr/bin/env"
export SB2_RUST_USE_REAL_EXECVP=Yes
export SB2_RUST_USE_REAL_FN=Yes
#export SB2_RUST_NO_SPAWNVP=Yes

# NOTE: add exports back in here (from git history) if they end up being necessary

%ifnarch %ix86
export HOST_CC=host-cc
export HOST_CXX=host-cxx
export CC_i686_unknown_linux_gnu=$HOST_CC
export CXX_i686_unknown_linux_gnu=$HOST_CXX
%endif

# Set meego cross compilers
export PATH=/opt/cross/bin/:$PATH
export CARGO_TARGET_ARMV7_UNKNOWN_LINUX_GNUEABIHF_LINKER=armv7hl-meego-linux-gnueabi-gcc
export CC_armv7_unknown_linux_gnueabihf=armv7hl-meego-linux-gnueabi-gcc
export CXX_armv7_unknown_linux_gnueabihf=armv7hl-meego-linux-gnueabi-g++
export AR_armv7_unknown_linux_gnueabihf=armv7hl-meego-linux-gnueabi-ar
export CARGO_TARGET_AARCH64_UNKNOWN_LINUX_GNU_LINKER=aarch64-meego-linux-gnu-gcc
export CC_aarch64_unknown_linux_gnu=aarch64-meego-linux-gnu-gcc
export CXX_aarch64_unknown_linux_gnu=aarch64-meego-linux-gnu-g++
export AR_aarch64_unknown_linux_gnu=aarch64-meego-linux-gnu-ar

# Set QMAKE for qmetaobject-rs builder, because for some reason it appears to
# get stuck after failing `qmake6` otherwise:
#   qmake returned with error:
#   /usr/bin/env: 'qmake6'
# https://github.com/woboq/qmetaobject-rs/blob/master/qttypes/build.rs#L41-L63
export QMAKE=qmake

# vim: set ft=spec:
