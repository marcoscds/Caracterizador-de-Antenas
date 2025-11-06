[app]

title = Caracterizador de Antenas
package.name = myapp
package.domain = org.test
source.dir = .

source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3,kivy,pyjnius,numpy,matplotlib,pillow,requests
p4a.fork = kivy
bootstrap = sdl2

icon.filename = icone.png
android.archs = arm64-v8a, armeabi-v7a

orientation = portrait
fullscreen = 0

android.permissions = BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_SCAN,BLUETOOTH_CONNECT,ACCESS_COARSE_LOCATION,ACCESS_FINE_LOCATION,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,INTERNET

android.api = 33
android.minapi = 26
android.ndk = 27


p4a.extra_env_vars = CFLAGS=-std=c++17
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
