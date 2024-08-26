[app]

# (str) Title of your application
title = File Converter

# (str) Package name
package.name = file-converter

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ogg

# (list) List of inclusions using pattern matching
source.include_patterns = data/*.png, sound/*.ogg

# (list) Source files to exclude (let empty to not exclude anything)
# source.exclude_exts = spec

# (list) List of directories to exclude (let empty to not exclude anything)
# source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern matching
# source.exclude_patterns = license, images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
requirements = python3,kivy,opencv-python-headless,Pillow

# (str) Custom source folders for requirements
# requirements.source.kivy = ../../kivy

# (list) Garden requirements
# garden_requirements =

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (str) Path to the Android SDK
# android.sdk_path = /path/to/android/sdk

# (str) Path to the Android NDK
# android.ndk_path = /path/to/android/ndk

# (str) Android NDK version
android.ndk = 25

# (str) Android SDK version
android.sdk = 33

# (str) Android API level
android.api = 33

# (str) Android NDK API level
android.ndk_api = 25

# (list) Permissions
android.permissions = INTERNET, CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (bool) Build the app in debug mode (default is True)
# android.debug = True

# (str) Application package
# android.package = org.example.fileconverter

# (str) Application entry point
# android.entrypoint = main

# (bool) Enable GPU support (default is False)
# gpu = False

# (bool) Whether to use a custom language (default is False)
# custom_lang = False

# (str) Path to the custom language file
# lang.filename = %(source.dir)s/lang.kv

# (bool) Enable touchscreen support (default is True)
# touchscreen = True

# (str) Target architecture (default is 'armeabi-v7a')
# android.arch = armeabi-v7a

# (list) List of additional environment variables
# android.env_vars =

# (bool) Enable verbose output (default is False)
# verbose = False

# (bool) Enable app bundle (default is False)
# android.app_bundle = False

# (bool) Enable multi-dex support (default is False)
# android.multi_dex = False

# (list) List of additional files to include (e.g. data files)
# include_files =

# (list) List of directories to include (e.g. assets)
# include_dirs =

# (list) List of excluded files (e.g. temp files)
# exclude_files =

# (bool) Enable a single APK (default is False)
# android.single_apk = False
