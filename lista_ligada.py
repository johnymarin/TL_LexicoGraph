import re


class Nodo:
    tipos = {'bol': 'bool',
             'str': 'String',
             'num': 'num',
             'int': 'int',
             'dbl': 'double',
             'var': 'var'}
    variables = '*'
    constantes = ''
    separadores = {
        'com': '[,]',
        'pyc': '[;]',
        'dps': '[:]',
        'apt': '[\(]',
        'cpt': '[\)]',
        'act': '[\[]',
        'cct': '[\]]',
        'alv': '[\}]',
        'clv': '[\{]',
        'spc': ' ',
        'tab': '\t',
        'cre': '\r',
        'nli': '\n'}
    operadores = {
        'add': '[+]',
        'sub': '[-]',
        'mul': '[*]',
        'div': '[/]',
        'asi': '[=]',
        'eq ': '[=][=]',
        'neq': '[!][=]',
        'gt ': '[>]',
        'gte': '[>][=]',
        'lt ': '[<]',
        'lte': '[<][=]',
        'and': '[&][&]',
        'or ': '[|][|]',
        'not': '[!]',
        'aas': '[+][=]',
        'sas': '[-][=]',
        'mas': '[*][=]',
        'das': '[/][=]'
    }
    boleanos = {'tru': 'True',
                'fal': 'False'}

    # Funcion para inicialzar el objeto nodo
    def __init__(self, dato: str):
        self.dato = dato  # Asigna dato
        self.sgte = None  # Inicializa con liga nula

    @property
    def clase(self):
        if re.search(pattern=f"^({'|'.join(self.tipos.values())})$", string=self.dato):
            return 'tip'
        elif re.search(pattern=f"^({'|'.join(self.separadores.values())})$", string=self.dato):
            return 'sep'
        elif re.search(pattern=f"^({'|'.join(self.operadores.values())})$", string=self.dato):
            return 'opr'
        elif re.search(pattern=f"^({'|'.join(self.boleanos.values())})$", string=self.dato):
            return 'bol'
        elif re.search(pattern=f"^[a-zA-Z][a-zA-Z0-9_.]*$", string=self.dato):
            return 'var'
        elif re.search(pattern=f"(^[+-]?[0-9]*[.]?[0-9]*[e]?[+-]?[0-9]$|^\".*\"$)", string=self.dato):
            return 'con'
        else:
            return 'err'


class ListaLigada:

    # Funcion para inicialzar el objeto lista ligada
    def __init__(self, nodos=None):
        self.cabeza: Nodo = None

    def __repr__(self):
        nodo = self.cabeza
        nodos = []
        while nodo is not None:
            nodos.append("{clase}:{dato}".format(clase=str(nodo.clase), dato=str(nodo.dato)))
            nodo = nodo.sgte
        nodos.append("Nulo")
        return "-> ".join(nodos)

    def __iter__(self):
        nodo = self.cabeza
        while nodo is not None:
            yield nodo
            nodo = nodo.sgte

    def encolar(self, nodo):
        if not self.cabeza:
            self.cabeza = nodo
            return
        for nodo_actual in self:
            pass
        nodo_actual.sgte = nodo
