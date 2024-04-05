project(uam_ros2_pkg)
cmake_minimum_required(VERSION 3.22)
find_package(ament_cmake_python REQUIRED)
find_package(ament_cmake_core REQUIRED)


ament_python_install_package(${PROJECT_NAME})

if(BUILD_TESTING)
  find_package(ament_cmake_pytest REQUIRED)
  set(_pytest_tests
    tests/test_a.py
    tests/test_b.py
    # Add other test files here
  )
  foreach(_test_path ${_pytest_tests})
    get_filename_component(_test_name ${_test_path} NAME_WE)
    ament_add_pytest_test(${_test_name} ${_test_path}
      APPEND_ENV PYTHONPATH=${CMAKE_CURRENT_BINARY_DIR}
      TIMEOUT 60
      WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    )
  endforeach()
endif()
