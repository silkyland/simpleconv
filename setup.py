from cx_Freeze import setup, Executable

setup(
    name="simpleconv",
    version="0.1",
    options={"build_exe": {"packages": ["tkinter", "pydub", "argparse"]}},
    executables=[Executable("conv.py", base=None)]
)
