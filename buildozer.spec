[app]
title = KERO Security
package.name = kerosecurity
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3==3.12.0, kivy, cython==3.0.10
orientation = portrait
osx.kivy_version = 2.1.0
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
[buildozer]
log_level = 2
warn_on_root = 1

