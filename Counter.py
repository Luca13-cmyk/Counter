#!/usr/local/bin/python3.8

from sys import argv
from collections import Counter

count = 0

def show_result(par, tar):
    try:
        if type(par) == str and par != '-A':
            args = int(par)
            print("\n")
            print(Counter(tar).most_common(args))
            print("\n")
            print("Apert CTRL + C para sair")
    except ValueError:
        print(f"O segundo argumento '{par}' n eh um inteiro")

try:
    target = argv[1]
    args = argv[2]
except IndexError:
    print("EX: python3.7 Counter.py <frase> -A")
    print("EX: python3.7 Counter.py <frase> 5")
else:
    if args == '-A':
        if len(target) > 20:
            print("para valores acima de 20 utilize: python3.7 Counter.py -B <number>")
            exit(1)
        print(Counter(target))
        exit(1)
    if target == '-B':
        while target != 'ok':
            if not count > 0:
                target = str(input("Digite o texto: "))
                show_result(args, target)
                count = 1
    else:
        show_result(args, target)

