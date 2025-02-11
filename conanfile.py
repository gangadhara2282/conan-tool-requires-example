from conan import ConanFile
from conan.tools.cmake import CMake

class TestConanProject(ConanFile):
    name = "test_conan_project"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"
    tool_requires = "gcc_toolchain/12.0@user/testing"
    exports_sources = "src/*"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
