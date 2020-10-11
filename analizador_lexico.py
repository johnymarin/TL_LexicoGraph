import re
import shlex

from lista_ligada import ListaLigada, Nodo

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


class AnalizadorLexico():

    def __init__(self):
        self.lista_liga = ListaLigada()
        self.estado_actual = None
        self.log_error = None

    def retornar_lista(self):
        return self.lista_liga

    def limpiar_lista(self):
        self.lista_liga.cabeza = None

    def analizar_linea(self, linea_texto: str = None):
        patron = f"({'|'.join(CARACTERES_ESPECIALES)})"
        palabras = re.sub(pattern=patron, repl=r" \1 ", string=linea_texto)
        palabras = shlex.split(palabras, posix=False)
        for p in palabras:
            nodo = Nodo(p)
            self.lista_liga.encolar(nodo)

    def establecer_estado(self, nodo_actual: Nodo):
        pass

    def retornar_texto(self):
        return "hola mundo"

    def retornar_texto_listal(self):
        return str(self.lista_liga)
