# -*- coding: utf-8 -*-
# Programa: Aparcamiento.py
# Objetivo: La compañía Genisys Inc cuenta con múltiples edificios en los cuáles brinda el servicio de estacionamiento
#de vehículos para clientes particulares.
# Repositorio: https://github.com/moralesklisban9/Examen.git
# Autor: Klisban Morales-0801199919211
# Fecha: *Viernes* 13 Marzo 2020
import sys
import platform
import datetime
import random

class Menu:
    """
    Esta clase nos despliega las opciones del menu Genisys
    """

    def __init__(self):
            """ Abre todas las listas """
            self.Vehiculo = list()
            self.opciones = {"1":self.ingreso,
                            "2":self.totalVehiculos,
                            "3":self.salidas,
                            "4":self.gananciasDia,
                            "5":self.salir
                            }

    def display_menu(self):
        """ Docstrim: esta def nos despliega el menu """
        print("""
             Bienvenido al Menu principal
            1:Insgreso de vehiculo
            2:Total de vehiculos
            3:Salidas
            4:Ganancias diarias
            5:salir
             """)

    def ingreso(self):
        """ Docstrim: Nos despleiga las opciones del vehiculo """
        placa = input("Ingrese placa del vehiculo:")
        marca = input("Ingrese marca del vehiculo:")
        modelo = input("Ingrese el modelo del vehiculo:")
        tipo_de_vehiculo = input("Ingrese tipo de vehiculo:")
        hora_ingreso = input("Ingrese hora de ingreso del vehiculo:")
        estado = input("Estado por defecto True:")
        print("El vehiculo se ha ingresado correctamente al sistema, ¡Excelente!")
        pass

    def totalVehiculos(self):
        """ Docstrim: funcion para el total de vehiculos """
        for vehi in vehiculos:
            print("placa vehicular: {0}\nmarca vehicular: '{1}'\nmodelo vehicular: {2}\ntipo vehiculo: {3}"
                  .format())

    def salida(self):
        """ Docstrim: Definir la salida del vehiculo """
         pass

    def gananciasDia(self):
        """ Docstrim: Definir las ganacias del dia """
         pass

    def salir(self):
          """ Docstrim: Cerrar """
        print("La aplicacion se ha cerrado")
        sys.exit(0)

    def horas(self):
        """ Docstrim: def para horas del vehiculo """
        horas_vehiculo=random(1,5)
        print(horas_vehiculo)