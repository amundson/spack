from spack import *

class Garply(Package):
    """Garply is a toy package"""
    homepage = "https://github.com/amundson/garply"
    url      = "http://compacc.fnal.gov/~amundson/garply-1.0.tar.gz"

    version('1.0', '13a24801512e5b577afde076d2e908d3')

    def install(self, spec, prefix):
        cmake(".", *std_cmake_args)
        make()
        make("install")
