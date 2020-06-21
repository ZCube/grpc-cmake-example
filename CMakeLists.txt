cmake_minimum_required(VERSION 3.0)
project(Project CXX)

if(WIN32)
  add_definitions(-D_WIN32_WINNT=0x600)
endif()

set(CMAKE_CXX_STANDARD 11)

# https://github.com/conan-io/cmake-conan/raw/v0.15/conan.cmake
include(cmake/conan.cmake)

conan_add_remote(NAME zcube INDEX 1
            URL https://api.bintray.com/conan/zcube/conan-public)

conan_cmake_run(CONANFILE conanfile.py
                BASIC_SETUP CMAKE_TARGETS
                BUILD missing)

include(${CMAKE_BINARY_DIR}/cmake/grpc.cmake)

add_executable(main main.cpp helloworld.proto)
target_link_libraries(main CONAN_PKG::grpc)
grpc_generate(TARGET main)
