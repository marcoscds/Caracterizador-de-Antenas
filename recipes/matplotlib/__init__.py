from pythonforandroid.recipes.matplotlib import MatplotlibRecipe

class FixedMatplotlibRecipe(MatplotlibRecipe):
    # Corrige o empacotamento da libc++_shared.so
    need_stl_shared = True

    # Força backend sem interface gráfica (necessário para Android)
    def get_recipe_env(self, arch=None, **kwargs):
        env = super().get_recipe_env(arch, **kwargs)
        env["MPLBACKEND"] = "Agg"  # evita dependência em tkinter ou qt
        env["MATPLOTLIBRC"] = "/data/data/org.kivy.matplotlib/matplotlibrc"
        return env

    # Nome interno da recipe (opcional, mas útil)
    name = "matplotlib"

recipe = FixedMatplotlibRecipe()
