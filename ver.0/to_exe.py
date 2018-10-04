# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 18:19:23 2018

@author: UARTman
"""

from cx_Freeze import setup, Executable

import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

'''
options = {
    'build_exe': {
        'include_files':[
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
         ],
    },
}
'''

base = None
setup(
    name = "Генератор графов",
    version = "0",
    description = "Генератор графов",
    executables = [Executable("TkInterFace.py")]
    #,options=options
)
