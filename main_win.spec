# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import copy_metadata

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('*.py', '.'),
        ('Icon\icon.ico','.'),]
        +
        copy_metadata('imageio') # fixes pyinstaller for `import moviepy`
        ,
    hiddenimports=[
        'tkinter',
        'imageio_ffmpeg',
        'os',
        'sys',
        'moviepy',
        'numpy',
        'imageIO'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    # a.zipfiles,
    a.datas,
    [],
    # exclude_binaries=True,
    # you must not have exclude_binaries as true or it'll make nothing
    name='Audio Unifier Win',
    description='Converts media files into selected format',
    author='Jabulani Ndhlovu',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='D:\Git_Repositories\Audio-Unifier\Icon\icon.ico',
)
