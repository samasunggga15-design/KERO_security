[app]

# (str) Title of your application
title = KERO Security

# (str) Package name
package.name = kerosecurity

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# CAUTION: Removed "android" from requirements to prevent pip build failure
requirements = python3, kivy

# (str) Custom source folders for requirements
#requirements.source.kivy = ../kivy

# (list) Garden requirements
#garden_requirements =

# (list) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientations (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# =============================================================================
# Android specific
# =============================================================================

# (bool) Accept SDK license without prompting
android.accept_sdk_license = True

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android API to target
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (list) Android architectures to build for
android.archs = armeabi-v7a, arm64-v8a

# (bool) automatically clean build cell on start
buildozer.clean = True
