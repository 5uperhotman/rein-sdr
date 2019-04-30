INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_DIODE Diode)

FIND_PATH(
    DIODE_INCLUDE_DIRS
    NAMES Diode/api.h
    HINTS $ENV{DIODE_DIR}/include
        ${PC_DIODE_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    DIODE_LIBRARIES
    NAMES gnuradio-Diode
    HINTS $ENV{DIODE_DIR}/lib
        ${PC_DIODE_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(DIODE DEFAULT_MSG DIODE_LIBRARIES DIODE_INCLUDE_DIRS)
MARK_AS_ADVANCED(DIODE_LIBRARIES DIODE_INCLUDE_DIRS)

