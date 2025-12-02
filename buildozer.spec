[app]

# Título e pacote
title = Caracterizador de Antenas
package.name = antenasapp
package.domain = org.marcossilva

# Código-fonte
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Requisitos (versões compatíveis com p4a e NDK 23b)
requirements = python3==3.11,kivy==2.2.1,numpy@https://github.com/vrenken/numpy-android/archive/refs/tags/v1.26.4.zip,matplotlib,setuptools,pillow,pyjnius,requests


# Ícone e presplash
icon.filename = icone.png
#presplash.filename = %(source.dir)s/Splash.png
android.presplash_color = #F6F6F6

# Orientação
orientation = portrait
fullscreen = 0

# Permissões Android
android.permissions = INTERNET,BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_CONNECT,BLUETOOTH_SCAN,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,BLUETOOTH_SCAN,ACCESS_COARSE_LOCATION,ACCESS_FINE_LOCATION,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# API e NDK
android.api = 31
android.minapi = 24
android.ndk = 25b
android.ndk_api = 24

# Armazenamento
android.private_storage = True
android.accept_sdk_license = True
android.archs = arm64-v8a
android.allow_backup = True

# Bootstrap e branch p4a
p4a.bootstrap = sdl2
p4a.branch = develop

[p4a]
git_url = https://github.com/kivy/python-for-android.git
git_branch = master


[buildozer]
log_level = 2
warn_on_root = 1
