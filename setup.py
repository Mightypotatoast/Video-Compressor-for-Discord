# commande à taper en ligne de commande après la sauvegarde de ce fichier:
# python setup.py build

from cx_Freeze import setup, Executable

executables = [
    Executable(script="main.py", icon="/img/discord.ico", base="Win32GUI")
]
# ne pas mettre "base = ..." si le programme n'est pas en mode graphique

buildOptions = dict(
    includes=["tkinter", "ffmpeg"],
    include_files=["./bin"]
)

setup(
    name="TransCord",
    version="1.2",
    description="Transcode video files to fit discord weight limit",
    author="MightyPotatoast",
    options=dict(build_exe=buildOptions),
    executables=executables
)
