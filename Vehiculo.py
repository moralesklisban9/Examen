# -*- coding: utf-8 -*-
# Autor: Klisban Morales 0801199919211
# Repositorio: https://github.com/moralesklisban9/Examen.git
from datetime import datetime, timedelta
plus_five_hours = datetime.now() + timedelta(hours=5)


class Vehiculo:

    hora = 0:
    """
    representa un vehiculo
    """

    def __init__(self, placa, marca, modelo, tipo):
        """ Inicializar los objetos del vehiculo """
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.Hora_Entrada = hour()
        self.Hora_Salida = hour()