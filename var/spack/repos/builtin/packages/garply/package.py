from spack import *


class Garply(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "http://compacc.fnal.gov/~amundson/garply-1.0.tar.gz"

    version('2.0.0', git='git@github.com:amundson/garply.git',
                        tag='v2.0.0')
    version('1.0', '13a24801512e5b577afde076d2e908d3')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
