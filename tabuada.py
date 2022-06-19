#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10."""
__version__ = "0.1.1"
__author__ = "Jorge Reiis"

base = list(range(1, 11))

for numero in base:
    print('{:-^26}'.format(' Tabuada do ' + str(numero)+' '))

    for num in base:
        print('{} x {} = {}'.format(numero, num, numero * num))
