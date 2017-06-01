#!/usr/bin/env python
# -*- coding: utf-8 -*-

from parser import ParserCsv
import json


def main():
    parser = ParserCsv()
    estructura_archivo = parser.get_estructura_archivo("base_excel_5.csv")
    lista = []
    for item in estructura_archivo:
        datos = json.dumps(item)
        lista.append(datos)
    print lista

if __name__ == "__main__":
    main()
