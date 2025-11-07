from pythonforandroid.recipe import Recipe
from pythonforandroid.toolchain import shprint
import sh

class HarfbuzzPatchedRecipe(Recipe):
    version = "5.3.1"
    url = "https://github.com/harfbuzz/harfbuzz/archive/refs/tags/{version}.tar.gz"

    def build_arch(self, arch):
        env = self.get_recipe_env(arch)
        env["CFLAGS"] += " -Wno-error=cast-function-type-strict"
        env["CXXFLAGS"] += " -Wno-error=cast-function-type-strict"
        shprint(sh.autoconf)
        shprint(sh.configure, "--with-freetype", _env=env)
        shprint(sh.make, "-j4", _env=env)

recipe = HarfbuzzPatchedRecipe()
