.. currentmodule:: vor12

========================
Install OpenCV3 from Git
========================

Problem:

OpenCV2 only works with Python2, not Python3.
OpenCV3 only works with Python3.
PyAX-12 only works with Python3.
OpenCV3 is not included in Debian8.

See:

- https://blog.kevin-brown.com/programming/2014/09/27/building-and-installing-opencv-3.html
- http://stackoverflow.com/questions/20953273/install-opencv-for-python-3-3
- http://stackoverflow.com/questions/26489867/opencv-for-python-3-x-under-windows


Get the source code (in the current directory)::

    git clone https://github.com/Itseez/opencv.git
    cd opencv
    git checkout tags/3.0.0 


Build (in my home directory)::

    mkdir build
    cd build
    mkdir ~/bin/opencv3
    cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=~/bin/opencv3 -D PYTHON_EXECUTABLE=$(which python3) ..
    ccmake .      # see the following "cmake options" section
    make -j2
    make install


ccmake options::

    ANT_EXECUTABLE                   /usr/bin/ant
    BUILD_CUDA_STUBS                 OFF
    BUILD_DOCS                       OFF
    BUILD_EXAMPLES                   OFF
    BUILD_JASPER                     OFF
    BUILD_JPEG                       OFF
    BUILD_OPENEXR                    OFF
    BUILD_PACKAGE                    ON
    BUILD_PERF_TESTS                 OFF
    BUILD_PNG                        OFF
    BUILD_SHARED_LIBS                ON
    BUILD_TBB                        OFF
    BUILD_TESTS                      OFF
    BUILD_TIFF                       OFF
    BUILD_WITH_DEBUG_INFO            ON
    BUILD_WITH_DYNAMIC_IPP           OFF
    BUILD_ZLIB                       OFF
    BUILD_opencv_apps                ON
    BUILD_opencv_calib3d             ON
    BUILD_opencv_core                ON
    BUILD_opencv_features2d          ON
    BUILD_opencv_flann               ON
    BUILD_opencv_hal                 ON
    BUILD_opencv_highgui             ON
    BUILD_opencv_imgcodecs           ON
    BUILD_opencv_imgproc             ON
    BUILD_opencv_java                OFF
    BUILD_opencv_ml                  ON
    BUILD_opencv_objdetect           ON
    BUILD_opencv_photo               ON
    BUILD_opencv_python2             OFF
    BUILD_opencv_python3             ON
    BUILD_opencv_shape               ON
    BUILD_opencv_stitching           ON
    BUILD_opencv_superres            ON
    BUILD_opencv_ts                  ON
    BUILD_opencv_video               ON
    BUILD_opencv_videoio             ON
    BUILD_opencv_videostab           ON
    BUILD_opencv_world               OFF
    BZIP2_LIBRARIES                  BZIP2_LIBRARIES-NOTFOUND
    CLAMDBLAS_INCLUDE_DIR            CLAMDBLAS_INCLUDE_DIR-NOTFOUND
    CLAMDBLAS_ROOT_DIR               CLAMDBLAS_ROOT_DIR-NOTFOUND
    CLAMDFFT_INCLUDE_DIR             CLAMDFFT_INCLUDE_DIR-NOTFOUND
    CLAMDFFT_ROOT_DIR                CLAMDFFT_ROOT_DIR-NOTFOUND
    CMAKE_BUILD_TYPE                 RELEASE
    CMAKE_CONFIGURATION_TYPES        Debug;Release
    CMAKE_INSTALL_PREFIX             /home/jeremie/bin/opencv3
    CUDA_BUILD_CUBIN                 OFF
    CUDA_BUILD_EMULATION             OFF
    CUDA_HOST_COMPILER               /usr/bin/gcc-4.9
    CUDA_SDK_ROOT_DIR                CUDA_SDK_ROOT_DIR-NOTFOUND
    CUDA_SEPARABLE_COMPILATION       OFF
    CUDA_TOOLKIT_ROOT_DIR            CUDA_TOOLKIT_ROOT_DIR-NOTFOUND
    CUDA_VERBOSE_BUILD               OFF
    EIGEN_INCLUDE_PATH               /usr/include/eigen3
    ENABLE_AVX                       OFF
    ENABLE_AVX2                      OFF
    ENABLE_COVERAGE                  OFF
    ENABLE_FAST_MATH                 OFF
    ENABLE_FMA3                      OFF
    ENABLE_IMPL_COLLECTION           OFF
    ENABLE_NOISY_WARNINGS            OFF
    ENABLE_OMIT_FRAME_POINTER        ON
    ENABLE_POPCNT                    OFF
    ENABLE_PRECOMPILED_HEADERS       ON
    ENABLE_PROFILING                 OFF
    ENABLE_SOLUTION_FOLDERS          OFF
    ENABLE_SSE                       ON
    ENABLE_SSE2                      ON
    ENABLE_SSE3                      ON
    ENABLE_SSE41                     OFF
    ENABLE_SSE42                     OFF
    ENABLE_SSSE3                     OFF
    EXECUTABLE_OUTPUT_PATH           /home/jeremie/sandbox/opencv3/opencv/build/bin
    GENERATE_ABI_DESCRIPTOR          OFF
    GIGEAPI_INCLUDE_PATH             GIGEAPI_INCLUDE_PATH-NOTFOUND
    GIGEAPI_LIBRARIES                GIGEAPI_LIBRARIES-NOTFOUND
    INSTALL_CREATE_DISTRIB           OFF
    INSTALL_C_EXAMPLES               OFF
    INSTALL_PYTHON_EXAMPLES          ON
    INSTALL_TESTS                    OFF
    INSTALL_TO_MANGLED_PATHS         OFF
    OPENCV_CONFIG_FILE_INCLUDE_DIR   /home/jeremie/sandbox/opencv3/opencv/build
    OPENCV_EXTRA_MODULES_PATH        
    OPENCV_WARNINGS_ARE_ERRORS       OFF
    OPENEXR_INCLUDE_PATH             /usr/include/OpenEXR
    PVAPI_INCLUDE_PATH               PVAPI_INCLUDE_PATH-NOTFOUND
    PYTHON2_EXECUTABLE               /usr/bin/python3
    PYTHON2_INCLUDE_DIR              /usr/include/python3.4m
    PYTHON2_INCLUDE_DIR2             
    PYTHON2_LIBRARY                  /usr/lib/x86_64-linux-gnu/libpython3.4m.so
    PYTHON2_LIBRARY_DEBUG            
    PYTHON2_NUMPY_INCLUDE_DIRS       /usr/lib/python3/dist-packages/numpy/core/include
    PYTHON2_PACKAGES_PATH            lib/python3.4/dist-packages
    PYTHON3_EXECUTABLE               /usr/bin/python3.4
    PYTHON3_INCLUDE_DIR              /usr/include/python3.4m
    PYTHON3_INCLUDE_DIR2             
    PYTHON3_LIBRARY                  /usr/lib/x86_64-linux-gnu/libpython3.4m.so
    PYTHON3_LIBRARY_DEBUG            
    PYTHON3_NUMPY_INCLUDE_DIRS       /usr/lib/python3/dist-packages/numpy/core/include
    PYTHON3_PACKAGES_PATH            lib/python3.4/dist-packages
    VTK_DIR                          VTK_DIR-NOTFOUND
    WEBP_INCLUDE_DIR                 WEBP_INCLUDE_DIR-NOTFOUND
    WITH_1394                        ON 
    WITH_CLP                         OFF
    WITH_CUBLAS                      OFF
    WITH_CUDA                        OFF
    WITH_CUFFT                       OFF
    WITH_EIGEN                       ON
    WITH_FFMPEG                      ON
    WITH_GDAL                        OFF
    WITH_GIGEAPI                     ON
    WITH_GPHOTO2                     ON
    WITH_GSTREAMER                   ON
    WITH_GSTREAMER_0_10              OFF
    WITH_GTK                         ON
    WITH_GTK_2_X                     OFF
    WITH_IPP                         ON
    WITH_IPP_A                       OFF
    WITH_JASPER                      ON
    WITH_JPEG                        ON
    WITH_LIBV4L                      ON
    WITH_NVCUVID                     OFF
    WITH_OPENCL                      ON
    WITH_OPENCLAMDBLAS               ON
    WITH_OPENCLAMDFFT                ON
    WITH_OPENCL_SVM                  OFF
    WITH_OPENEXR                     ON
    WITH_OPENGL                      OFF
    WITH_OPENMP                      OFF
    WITH_OPENNI                      OFF
    WITH_OPENNI2                     OFF
    WITH_PNG                         ON
    WITH_PTHREADS_PF                 OFF
    WITH_PVAPI                       ON
    WITH_QT                          OFF
    WITH_TBB                         OFF
    WITH_TIFF                        ON
    WITH_UNICAP                      OFF
    WITH_V4L                         ON
    WITH_VTK                         ON
    WITH_WEBP                        ON
    WITH_XIMEA                       OFF
    WITH_XINE                        OFF


Test::

    ipython3
    import sys
    sys.path.append("/home/jeremie/bin/opencv3/lib/python3.4/dist-packages/")
    import cv2

    print(cv2.__version__)

