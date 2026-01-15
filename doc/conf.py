import os
import sys

# Ajout du chemin src/ pour autodoc
sys.path.insert(0, os.path.abspath("../src"))

project = "sl29.games.2048"
extensions = ["sphinx.ext.autodoc"]
templates_path = ["_templates"]
exclude_patterns = ["_build"]
#html_theme = "alabaster"
