#!/usr/bin/python3
#Author: Oliver Vilchis
#Programa que se encargara de presentar las funciones de un cajero automatico, donde se podran realizar tres acciones "Consultar saldo,retirar saldo y visualizar el historico de acciones"

from Cajero import Cajero

def main():
    """Metodo que inicializa el programa"""
    cajero = Cajero()
    cajero()

if __name__ == '__main__':
    main()
