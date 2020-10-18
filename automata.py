from automat import MethodicalMachine
import logging
from collections import deque

logging.basicConfig(filename='automata.log', filemode='w', level=logging.WARNING)

ESTADOS = {
    '00': 'particion 00',
    '01': 'particion 01',
    '02': 'particio 02',
    '03': 'particion 03',
    '04': 'particion 04',
    '05': 'particion 05',
    '06': 'particion 06',
    '07': 'particion 07',
    '08': 'particion 08',
    '09': 'particion 09',
    '10': 'particion 10',
    '11': 'particion 11',
    '12': 'particion 12',
}

class Automata(object):
    def __init__(self):
        self.estado_actual: str = ESTADOS['00']

    def establecer_estado(self, nodo,  linea):
        simbolo = nodo.simbolo
        dato = nodo.dato
        if self.estado_actual == ESTADOS['00']:
            if simbolo in ('tip'):
                self.estado_actual = ESTADOS['04']
            elif simbolo in ('var'):
                self.estado_actual = ESTADOS['05']
            elif simbolo in ('pyc'):
                self.estado_actual = ESTADOS['00']
            else:
                self.explicar_error(simbolo, dato, linea)
        elif self.estado_actual == ESTADOS['02']:
            if simbolo in ('com'):
                self.estado_actual = ESTADOS['04']
            elif simbolo in ('opr'):
                self.estado_actual = ESTADOS['09']
            elif simbolo in ('pyc'):
                self.estado_actual = ESTADOS['00']
            else:
                self.explicar_error(simbolo, dato, linea)
        elif self.estado_actual == ESTADOS['03']:
            if simbolo in ('bol', 'var', 'con'):
                self.estado_actual = ESTADOS['10']
            elif simbolo in ('sep'):
                self.estado_actual = ESTADOS['03']
            else:
                self.explicar_error(simbolo, dato, linea)
        elif self.estado_actual == ESTADOS['04']:
            if simbolo in ('var'):
                self.estado_actual = ESTADOS['06']
            else:
                self.explicar_error(simbolo, dato, linea)
        elif self.estado_actual == ESTADOS['05']:
            if simbolo in ('igu', 'opr'):
                self.estado_actual = ESTADOS['03']
            elif simbolo in ('sep'):
                self.estado_actual = ESTADOS['05']
            elif simbolo in ('pyc'):
                self.estado_actual = ESTADOS['00']
            else:
                self.explicar_error(simbolo, dato, linea)
        elif self.estado_actual == ESTADOS['06']:
            if simbolo in ('com'):
                self.estado_actual = ESTADOS['04']
            elif simbolo in ('igu'):
                self.estado_actual = ESTADOS['08']
            elif simbolo in ('pyc'):
                self.estado_actual = ESTADOS['00']
            else:
                self.explicar_error(simbolo, dato, linea)
        elif self.estado_actual == ESTADOS['07']:
            if simbolo in ('com'):
                self.estado_actual = ESTADOS['04']
            elif simbolo in ('opr'):
                self.estado_actual = ESTADOS['08']
            elif simbolo in ('log'):
                self.estado_actual = ESTADOS['09']
            elif simbolo in ('pyc'):
                self.estado_actual = ESTADOS['00']
            else:
                self.explicar_error(simbolo, dato, linea)
        elif self.estado_actual == ESTADOS['09']:
            if simbolo in ('bol', 'var', 'con'):
                self.estado_actual = ESTADOS['07']
            elif simbolo in ('sep'):
                self.estado_actual = ESTADOS['08']
            else:
                self.explicar_error(simbolo, dato, linea)
        elif self.estado_actual == ESTADOS['09']:
            if simbolo in ('bol', 'var', 'con'):
                self.estado_actual = ESTADOS['02']
            elif simbolo in ('sep'):
                self.estado_actual = ESTADOS['09']
            else:
                self.explicar_error(simbolo, dato, linea)
        elif self.estado_actual == ESTADOS['10']:
            if simbolo in ('opr'):
                self.estado_actual = ESTADOS['03']
            elif simbolo in ('log'):
                self.estado_actual = ESTADOS['12']
            elif simbolo in ('pyc'):
                self.estado_actual = ESTADOS['00']
            else:
                self.explicar_error(simbolo, dato, linea)
        elif self.estado_actual == ESTADOS['11']:
            if simbolo in ('opr'):
                self.estado_actual = ESTADOS['12']
            elif simbolo in ('pyc'):
                self.estado_actual = ESTADOS['00']
            else:
                self.explicar_error(simbolo, dato, linea)
        elif self.estado_actual == ESTADOS['12']:
            if simbolo in ('bol', 'var', 'con'):
                self.estado_actual = ESTADOS['11']
            elif simbolo in ('sep'):
                self.estado_actual = ESTADOS['12']
            else:
                self.explicar_error(simbolo, dato, linea)

    def explicar_error(self, simbolo: str, dato: str, linea:int):
        logging.error(f"error en la linea {linea}: {self.estado_actual} se recibio un {dato} es del tipo {simbolo}")


