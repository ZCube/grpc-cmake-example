from conans import ConanFile, CMake

class GrpcExampleConan(ConanFile):
   settings = "os", "compiler", "build_type", "arch"
   requires = "grpc/1.29.1@zcube/stable", "openssl/1.1.1g", "zlib/1.2.11"
   generators = "cmake"
   default_options = {}

   def imports(self):
       self.copy("*.cmake", dst="cmake", src="cmake") # From cmake to cmake
