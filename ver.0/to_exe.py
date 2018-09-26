# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 18:19:23 2018

@author: UARTman
"""

from cx_Freeze import setup, Executable

setup(
    name = "Генератор графов",
    version = "0",
    description = "Генератор графов",
    executables = [Executable("Main.py")]
)