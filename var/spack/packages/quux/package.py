from spack import *

class Quux(Package):
    """Quux is a toy package"""
    homepage = "https://github.com/amundson/quux"
    url      = "http://compacc.fnal.gov/~amundson/quux-1.0.tar.gz"

    version('1.0', 'e64c0dfbfdf43c17cd6aeeef79058734')

    depends_on("cmake@3.0:")
    depends_on("garply")

    def install(self, spec, prefix):
        cmake(".", *std_cmake_args)
        make()
        make("install")
