from typing import Dict

from automat import MethodicalMachine
import logging
from collections import deque

# Crear el logger
logger_modulo = logging.getLogger('main_logger.automata')


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

PILA_P = deque()
PILA_A = deque()
PILA_L = deque()
PILA_C = deque()



class Automata(object):


    balances: Dict[str, bool]

    def __init__(self):
        self.estado_actual: str = ESTADOS['00']
        self.balances: Dict[str, bool] = {'p': True, 'a': True, 'l': True, 'c': True}
        self.pilas = {'p': PILA_P, 'a': PILA_A, 'l': PILA_L, 'c': PILA_C}



    def retornar_simbolo_pila(self, dato):
        if dato in '()':
            return  'p'
        elif dato in '<>':
            return 'a'
        elif dato in '{}':
            return 'l'
        elif dato in '[]':
            return 'c'
        else:
            return None

    def verificar_pilas_vacias(self):
        for simbolo_pila in 'palc':
            if self.pilas.get(simbolo_pila):
                self.explicar_error_balance(simbolo_pila=simbolo_pila)
        return None

    def verificar_balance(self, dato):
        simbolo_pila = self.retornar_simbolo_pila(dato)
        if simbolo_pila:
            if self.balances.get(simbolo_pila):
                if dato in ('(','<','{','['):
                    self.pilas.get(simbolo_pila).append(simbolo_pila)
                elif dato in (')','>','}',']'):
                    if self.pilas.get(simbolo_pila):
                        self.pilas.get(simbolo_pila).pop()
                    else:
                        self.balances[simbolo_pila] = False
                        self.explicar_error_balance(dato=dato)
            else:
                self.explicar_error_balance()
        return

    def establecer_estado(self, nodo,  linea):
        simbolo = nodo.simbolo
        dato = nodo.dato
        self.verificar_balance(dato)

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
        logger_modulo.error(f"error de sintaxis en la linea {linea}: {self.estado_actual} se recibio un {dato} es del tipo {simbolo}")

    def explicar_error_balance(self, simbolo_pila: str = None, dato: str = None ):
        if simbolo_pila:
            logger_modulo.error(f"error de balanceo aun quedan {simbolo_pila} pendientes por cerrar")
        else:
            if dato:
                logger_modulo.error(f"error de balanceo  caracter de cierre {dato} cuando no existe caracter de apertura")
            else:
                logger_modulo.error(f"error de balanceo se intenta ingresar mas caracteres cuando el estado es desbalanceado")



