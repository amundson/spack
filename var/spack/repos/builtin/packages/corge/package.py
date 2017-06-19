from spack import *

class Corge(CMakePackage):
    """Corge is a toy package"""
    homepage = "https://github.com/amundson/corge"
    url      = "http://compacc.fnal.gov/~amundson/corge-1.0.tar.gz"

    version('2.0.0', git='https://github.com/amundson/corge.git',
            tag='v2.0.0')
    version('1.0.4', git='https://github.com/amundson/corge.git',
            tag='v1.0.4')
    version('1.0.3', git='https://github.com/amundson/corge.git',
            tag='v1.0.3')
    version('1.0.2', git='https://github.com/amundson/corge.git',
            tag='v1.0.2')
    version('1.0.1', git='https://github.com/amundson/corge.git',
            tag='v1.0.1')
    version('1.0', 'c83ec110f677b67e0496260ccc7ceb81')
    version('master', git='https://github.com/amundson/corge.git')

    depends_on("cmake@3.0:")
    depends_on("quux")

