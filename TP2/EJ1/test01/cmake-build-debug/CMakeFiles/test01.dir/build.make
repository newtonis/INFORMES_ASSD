# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.13

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "C:\Program Files\JetBrains\CLion 2019.1\bin\cmake\win\bin\cmake.exe"

# The command to remove a file.
RM = "C:\Program Files\JetBrains\CLion 2019.1\bin\cmake\win\bin\cmake.exe" -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = C:\Users\newto\INFORMES_ASSD\TP2\EJ1\test01

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = C:\Users\newto\INFORMES_ASSD\TP2\EJ1\test01\cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/test01.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/test01.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/test01.dir/flags.make

CMakeFiles/test01.dir/main.cpp.obj: CMakeFiles/test01.dir/flags.make
CMakeFiles/test01.dir/main.cpp.obj: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:\Users\newto\INFORMES_ASSD\TP2\EJ1\test01\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/test01.dir/main.cpp.obj"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\X86_64~2.EXE  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\test01.dir\main.cpp.obj -c C:\Users\newto\INFORMES_ASSD\TP2\EJ1\test01\main.cpp

CMakeFiles/test01.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test01.dir/main.cpp.i"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\X86_64~2.EXE $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E C:\Users\newto\INFORMES_ASSD\TP2\EJ1\test01\main.cpp > CMakeFiles\test01.dir\main.cpp.i

CMakeFiles/test01.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test01.dir/main.cpp.s"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\X86_64~2.EXE $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S C:\Users\newto\INFORMES_ASSD\TP2\EJ1\test01\main.cpp -o CMakeFiles\test01.dir\main.cpp.s

# Object files for target test01
test01_OBJECTS = \
"CMakeFiles/test01.dir/main.cpp.obj"

# External object files for target test01
test01_EXTERNAL_OBJECTS =

test01.exe: CMakeFiles/test01.dir/main.cpp.obj
test01.exe: CMakeFiles/test01.dir/build.make
test01.exe: CMakeFiles/test01.dir/linklibs.rsp
test01.exe: CMakeFiles/test01.dir/objects1.rsp
test01.exe: CMakeFiles/test01.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=C:\Users\newto\INFORMES_ASSD\TP2\EJ1\test01\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable test01.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\test01.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/test01.dir/build: test01.exe

.PHONY : CMakeFiles/test01.dir/build

CMakeFiles/test01.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\test01.dir\cmake_clean.cmake
.PHONY : CMakeFiles/test01.dir/clean

CMakeFiles/test01.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" C:\Users\newto\INFORMES_ASSD\TP2\EJ1\test01 C:\Users\newto\INFORMES_ASSD\TP2\EJ1\test01 C:\Users\newto\INFORMES_ASSD\TP2\EJ1\test01\cmake-build-debug C:\Users\newto\INFORMES_ASSD\TP2\EJ1\test01\cmake-build-debug C:\Users\newto\INFORMES_ASSD\TP2\EJ1\test01\cmake-build-debug\CMakeFiles\test01.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/test01.dir/depend

