[app]
# (str) Title of your application
title = FileConverter

# (str) Package name
package.name = fileconverter

# (str) Package domain (should be a valid domain name, e.g. org.example)
package.domain = org.example

# (str) Source code where the main.py is located
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# (list) List of requirements
requirements = python3,kivy,numpy,opencv-python,pillow

# (str) Entry point for your application
entrypoint = main.py

# (str) Supported platforms (one or more of: android, ios, windows, macosx, linux)
platforms = android

# (bool) Whether to use a virtual environment for building
use_venv = true

# (str) Build mode (debug or release)
build_mode = release

# (str) Path to the build directory
build_dir = .buildozer

# (bool) Whether to use the Buildozer cache
use_cache = true

# (list) List of permissions required by your app
# Adding permissions for camera and file access
android.permissions = CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (str) Application version
version = 0.1

android.ndk = 27.0.0
