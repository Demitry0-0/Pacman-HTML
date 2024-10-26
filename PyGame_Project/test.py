from cx_Freeze import setup, Executable

executables = [Executable('main.py',
                          targetName='My_game.exe')]

includes = ['pygame', 'pygame_gui', 'os', 'sys', 'random', 'time', 'sqlite3', 'requests']

zip_include_packages = ['pygame', 'pygame_gui', 'os', 'sys', 'random', 'time', 'sqlite3', 'requests']

include_files = ['data/freesansbold.ttf']

options = {
    'build_exe': {
        'include_msvcr': True,
        'includes': includes,
        'zip_include_packages': zip_include_packages,
        'build_exe': 'build_windows',
        'include_files': include_files,
    }
}

setup(name='online_game',
      version='0.0.1',
      description='My game',
      executables=executables,
      options=options)
