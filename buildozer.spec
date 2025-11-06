[app]
title = Caracterizador de Antenas
package.name = myapp
package.domain = org.test
source.dir = .

source.include_exts = py,png,jpg,kv,atlas
version = 0.1

#  Correção 1: Remover versões fixas para evitar o Erro 404
requirements = python3,kivy,numpy,matplotlib,pillow,pyjnius,requests

p4a.local_recipes = %(cwd)s/recipes # OK (Assumindo que sua receita Matplotlib está lá)
p4a.fork = kivy
p4a.branch = master
p4a.bootstrap = sdl2
#  Fixar a âncora de Python (3.10 é OK, 3.11 seria ligeiramente melhor)
p4a.python_version = 3.10 
p4a.extra_env_vars = CFLAGS=-std=c++17 # OK (Solução C++ 17)

#  REMOVIDA: Linha redundante
# android.shared_libraries = libc++_shared.so 
android.archs = arm64-v8a, armeabi-v7a

android.api = 33
android.minapi = 26
#  Correção 2: Usar NDK moderno para evitar erros de C/C++
android.ndk = 27
#  REMOVIDA: Linha obsoleta
# android.ndk_api = 23

icon.filename = icone.png
orientation = portrait
fullscreen = 0

# Permissões são OK, apenas o formato é um pouco longo.
android.permissions = BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_SCAN,BLUETOOTH_CONNECT,ACCESS_COARSE_LOCATION,ACCESS_FINE_LOCATION,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,INTERNET

android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
