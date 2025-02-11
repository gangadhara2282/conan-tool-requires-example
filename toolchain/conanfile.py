from conan import ConanFile

class GccToolchainConan(ConanFile):
    name = "gcc_toolchain"
    version = "12.0"
    settings = "os", "arch"
    package_type = "application"

    def package_info(self):
        self.buildenv_info.define("CC", "/usr/bin/gcc")
        self.buildenv_info.define("CXX", "/usr/bin/g++")
