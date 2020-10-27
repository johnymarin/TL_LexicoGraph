import re
import shlex
import logging
import io
from lista_ligada import ListaLigada, Nodo
from automata import Automata

# Crear el logger
logger_modulo = logging.getLogger('main_logger.analizador_lexico')


CARACTERES_ESPECIALES = (
    '[/]',
    '[=][=]',
    '[-][=]',
    '[!][=]',
    '[>]',
    '[>][=]',
    '[<][=]',
    '[=]',
    '[<]',
    '[+]',
    '[-]',
    '[,]',
    '[;]',
    '[\(]',
    '[\)]',
    '[\{]',
    '[\}]',
    '[\]]',
    '[\]]',
    '[*]',
)



class AnalizadorLexico(object):

    def __init__(self):
        self.lista_liga = ListaLigada()
        self.automata = Automata()
        self.linea: int = 0
        self.linea_lista = ListaLigada()
        self.linea_errores: str = None
        self.log_error: str = None



    def retornar_lista(self):
        return self.lista_liga

    def limpiar(self):
        self.lista_liga.cabeza = None
        self.linea = 0
        self.linea_lista.cabeza = None
        self.automata = Automata()

    def analizar_linea(self, linea_texto: str = None):


        self.linea += 1
        self.linea_lista = ListaLigada()
        self.linea_errores = ''
        logger_modulo.info(f"Procesando la linea {self.linea} : {linea_texto}")

        patron = f"({'|'.join(CARACTERES_ESPECIALES)})"
        palabras = re.sub(pattern=patron, repl=r" \1 ", string=linea_texto)
        try:
            palabras = shlex.split(palabras, posix=False)
        except ValueError:
            logger_modulo.error(f"error en linea {self.linea}: falto cierre de parentesis")
            return
        for p in palabras:
            nodo = Nodo(p)
#            self.lista_liga.encolar(nodo)
            self.linea_lista.encolar(nodo)
            self.automata.establecer_estado(nodo, self.linea)
        logger_modulo.info(self.linea_lista)




    def retornar_texto(self):
        return "hola mundo"

    def retornar_texto_listal(self):
        return str(self.lista_liga)

    def verificar_balances(self):
        self.automata.verificar_pilas_vacias()
