import re
import shlex

from lista_ligada import ListaLigada, Nodo
from automata import Automata


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
    '[(]',
    '[)]',
    '[*]',
)



class AnalizadorLexico(object):

    def __init__(self):
        self.lista_liga = ListaLigada()
        self.automata = Automata()
        self.linea: int = 0
        self.log_error: str = None


    def retornar_lista(self):
        return self.lista_liga

    def limpiar_lista(self):
        self.lista_liga.cabeza = None

    def analizar_linea(self, linea_texto: str = None):
        self.linea += 1
        self.estado_actual = 'particion_00'
        patron = f"({'|'.join(CARACTERES_ESPECIALES)})"
        palabras = re.sub(pattern=patron, repl=r" \1 ", string=linea_texto)
        palabras = shlex.split(palabras, posix=False)
        for p in palabras:
            nodo = Nodo(p)
            self.lista_liga.encolar(nodo)
            self.automata.establecer_estado(nodo, self.linea)



    def retornar_texto(self):
        return "hola mundo"

    def retornar_texto_listal(self):
        return str(self.lista_liga)
