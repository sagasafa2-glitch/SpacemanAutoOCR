
[app]

title = Spaceman Auto OCR Monitor

package.name = spacemanautoocr

package.domain = org.spacemanautoocr

source.dir = .

source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

requirements = python3,kivy,charset-normalizer==2.1.1

orientation = portrait

fullscreen = 0

android.permissions = INTERNET

android.api = 35

android.minapi = 24

android.ndk_api = 24

android.archs = arm64-v8a

android.allow_backup = False

[buildozer]

log_level = 2

warn_on_root = 1
