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



class AnalizadorLexico(object):

    def __init__(self):
        self.lista_liga = ListaLigada()
        self.estado_actual = 'particion_00'
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
            self.establecer_estado(self, nodo.simbolo)

    def establecer_estado(self, simbolo: str):
        if self.estado_actual == 'particion_00':
            if simbolo in ('tip'):
                self.estado_actual = 'particion_04'
            elif simbolo in ('var'):
                self.estado_actual = 'particion_05'
            elif simbolo in ('pyc'):
                self.estado_actual = 'particion_00'
            else:
                self.explicar_error(simbolo)
        if self.estado_actual == 'particion_02':
            if simbolo in ('com'):
                self.estado_actual = 'particion_04'
            elif simbolo in ('opr'):
                self.estado_actual = 'particion_09'
            elif simbolo in ('pyc'):
                self.estado_actual = 'particion_00'
            else:
                self.explicar_error(simbolo)
        if self.estado_actual == 'particion_03':
            if simbolo in ('bol', 'var', 'con'):
                self.estado_actual = 'particion_10'
            elif simbolo in ('sep'):
                self.estado_actual = 'particion_03'
            else:
                self.explicar_error(simbolo)
        if self.estado_actual == 'particion_04':
            if simbolo in ('var'):
                self.estado_actual = 'particion_06'
            else:
                self.explicar_error(simbolo)
        if self.estado_actual == 'particion_05':
            if simbolo in ('igu', 'opr'):
                self.estado_actual = 'particion_03'
            elif simbolo in ('sep'):
                self.estado_actual = 'particion_05'
            elif simbolo in ('pyc'):
                self.estado_actual = 'particion_00'
            else:
                self.explicar_error(simbolo)
        if self.estado_actual == 'particion_06':
            if simbolo in ('com'):
                self.estado_actual = 'particion_04'
            elif simbolo in ('igu'):
                self.estado_actual = 'particion_08'
            elif simbolo in ('pyc'):
                self.estado_actual = 'particion_00'
            else:
                self.explicar_error(simbolo)
        if self.estado_actual == 'particion_07':
            if simbolo in ('com'):
                self.estado_actual = 'particion_04'
            elif simbolo in ('opr'):
                self.estado_actual = 'particion_08'
            elif simbolo in ('log'):
                self.estado_actual = 'particion_09'
            elif simbolo in ('pyc'):
                self.estado_actual = 'particion_00'
            else:
                self.explicar_error(simbolo)
        if self.estado_actual == 'particion_08':
            if simbolo in ('bol', 'var', 'con'):
                self.estado_actual = 'particion_07'
            elif simbolo in ('sep'):
                self.estado_actual = 'particion_08'
            else:
                self.explicar_error(simbolo)
        if self.estado_actual == 'particion_09':
            if simbolo in ('bol', 'var', 'con'):
                self.estado_actual = 'particion_02'
            elif simbolo in ('sep'):
                self.estado_actual = 'particion_09'
            else:
                self.explicar_error(simbolo)
        if self.estado_actual == 'particion_10':
            if simbolo in ('opr'):
                self.estado_actual = 'particion_03'
            elif simbolo in ('log'):
                self.estado_actual = 'particion_12'
            elif simbolo in ('pyc'):
                self.estado_actual = 'particion_00'
            else:
                self.explicar_error(simbolo)
        if self.estado_actual == 'particion_11':
            if simbolo in ('opr'):
                self.estado_actual = 'particion_12'
            elif simbolo in ('pyc'):
                self.estado_actual = 'particion_00'
            else:
                self.explicar_error(simbolo)
        if self.estado_actual == 'particion_12':
            if simbolo in ('bol', 'var', 'con'):
                self.estado_actual = 'particion_11'
            elif simbolo in ('sep'):
                self.estado_actual = 'particion_12'
            else:
                self.explicar_error(simbolo)



    def explicar_error(self, simbolo: str):
        pass

    def retornar_texto(self):
        return "hola mundo"

    def retornar_texto_listal(self):
        return str(self.lista_liga)
