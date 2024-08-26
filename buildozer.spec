[app]

# (str) Title of your application
title = File Converter

# (str) Package name
package.name = fileconverter

# (str) Package domain (should be your own domain)
package.domain = org.yourdomain

# (str) Source code where the main.py is located
source.dir = .

# (str) The main entry point of your application
source.include_exts = py,png,jpg,kv,atlas

# (str) Name of the main application file (e.g. main.py)
# Change it if your main file is named differently
main.py = main.py

# (str) The directory in which your icon is located
icon.filename = %(source.dir)s/icon.png

# (str) Supported orientations (one of landscape, sensorLandscape, portrait or all)
orientation = landscape,portrait,landscape-reverse,portrait-reverse

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# (str) Presplash background color (for .png files, using hex value)
presplash.color = #000000

# (str) Presplash image (e.g. 'res/presplash.png')
presplash.filename = %(source.dir)s/presplash.png

# (str) Adaptive icon of the application (used if Android API level is 26+ at runtime)
# icon.adaptive_foreground.filename = %(source.dir)s/icon_fg.png
# icon.adaptive_background.filename = %(source.dir)s/icon_bg.png

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, CAMERA

# (int) Android API to use
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 28

# (str) Android NDK version to use
android.ndk = 23b
# (list) Path to the Android NDK (optional)
# This is the path to the NDK directory. 
# If not specified, Buildozer will use the default version.



# (bool) Indicate if you want to create an x86 package
android.arch = armeabi-v7a

# (str) Android architecture
android.archs = arm64-v8a, armeabi-v7a

# (str) Application version
version = 1.0

# (str) Requirements for the app (comma separated)
requirements = python3,kivy,pillow

# (bool) Enable Android logcat output to the console
android.logcat = 1

# (str) An example of specifying requirements
# (list) python3requirements
# android.requirements = android

# (bool) Use the updated `pythonforandroid` toolchain
use_legacy_toolchain = 1

# (bool) Indicate whether to build for release
android.release = False

# (bool) Install the debug version of the APK on your device after building
android.debug_install = True

# (bool) Enable SDL2 support (required for Kivy >= 2.0.0)
android.add_sdl2 = True

# (bool) Enable Vibrate support (required for Kivy >= 2.0.0)
android.add_vibrate = False

# (bool) Include GStreamer libraries in the APK (required for Kivy >= 2.0.0)
android.add_gstreamer = False

# (bool) Copy the following files into the APK (required for Kivy >= 2.0.0)
android.add_assets = assets

# (str) The URL for the repository where the source code of the application is located
android.add_rctask = False

# (bool) Enable debug symbols in release builds
android.release_debug_symbols = 1

# (str) The directory where the pre-built APK will be placed
android.dist_dir = /dist

# (str) The number of threads to use during the build process
android.build_threads = 4
