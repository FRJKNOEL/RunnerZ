from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "votre_programme",
    version = "1",
    description = "Votre programme",
    executables = [Executable("Start_menu.py")],
)
