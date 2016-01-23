from spack import *

class Chef(Package):
    """FIXME: put a proper description of your package here."""
    homepage = "http://www.example.com"
    url      = "http://compacc.fnal.gov/~amundson/chef-2016-01-06.tar.bz2"

    version('2016-0', '1174747188063a965ea5e792f94038b3')

    depends_on("boost")
    depends_on("fftw+mpi")
    depends_on("python")
    depends_on("cmake")
    depends_on("py-numpy")

    def install(self, spec, prefix):
        options = []
        options.extend(std_cmake_args)
        options.extend(['-DBUILD_PARSER_MODULES=OFF'])

        cmake('.', *options)

        make()
        make("install")
