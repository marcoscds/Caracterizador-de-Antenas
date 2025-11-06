# Importa a classe da receita original do python-for-android
# Nota: O nome da classe deve ser MatplotlibRecipe
from pythonforandroid.recipes.matplotlib import MatplotlibRecipe

# Cria uma classe que herda a receita original
# Isso garante que todas as etapas de compilação originais sejam mantidas
class FixedMatplotlibRecipe(MatplotlibRecipe):
    
    # Esta linha é a correção crucial! 
    # Ela garante que a biblioteca C++ compartilhada (libc++_shared.so)
    # seja empacotada no APK, resolvendo o erro 'cannot locate symbol'.
    need_stl_shared = True
    
    # Opcional: Você pode manter o nome original da receita, mas usando
    # uma classe diferente, você pode garantir que o P4A use a sua.
    name = 'matplotlib'

# Você deve definir uma variável 'recipe' que aponta para a sua classe
# Essa variável é o ponto de entrada que o Python-for-Android usa.
recipe = FixedMatplotlibRecipe()
