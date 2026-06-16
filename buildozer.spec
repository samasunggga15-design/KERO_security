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
requirements = python3, kivy

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

# (list) Android architectures to build for (تم تقليلها للسرعة)
android.archs = arm64-v8a

# (list) Pattern to exclude from the APK (حذف ملفات التست لتقليل الحجم)
android.exclude_patterns = license,lib/python3.*/test/*,lib/python3.*/site-packages/*/tests/*

# (bool) automatically clean build cell on start
buildozer.clean = True
