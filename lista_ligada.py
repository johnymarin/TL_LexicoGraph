import re


class Nodo:
    SIMBOLOS_TIPO = {'bol': 'bool',
                     'str': 'String',
                     'num': 'num',
                     'int': 'int',
                     'dbl': 'double',
                     'var': 'var'}

    SIMBOLOS_COMA = {'com': '[,]', }
    SIMBOLOS_IGUAL = {'asi': '[=]', }
    SIMBOLOS_BOLEANO = {'tru': 'True',
                        'fal': 'False'}
    SIMBOLOS_SEPARADOR = {'apt': '[\(]',
                          'cpt': '[\)]',
                          'act': '[\[]',
                          'cct': '[\]]',
                          'alv': '[\}]',
                          'clv': '[\{]',
                          }
    SIMBOLOS_MATEMATICO = {'add': '[+]',
                           'sub': '[-]',
                           'mul': '[*]',
                           'div': '[/]',
                           }
    SIMBOLOS_LOGICO = {'eq ': '[=][=]',
                       'neq': '[!][=]',
                       'gt ': '[>]',
                       'gte': '[>][=]',
                       'lt ': '[<]',
                       'lte': '[<][=]',
                       'and': '[&][&]',
                       'or ': '[|][|]',
                       }
    SIMBOLOS_ASIGNAR = {'aas': '[+][=]',
                        'sas': '[-][=]',
                        'mas': '[*][=]',
                        'das': '[/][=]'
                        }
    SIMBOLOS_NEGACION = {'not': '[!]', }
    SIMBOLOS_PUNTOYCOMA = {'pyc': '[;]', }
    SIMBOLOS_DOSPUNTOS = {'dps': '[:]', }


    CLASE_SEPARADOR = {

        'spc': ' ',
        'tab': '\t',
        'cre': '\r',
        'nli': '\n'}

    CLASE_TIPO = {'bol': 'bool',
             'str': 'String',
             'num': 'num',
             'int': 'int',
             'dbl': 'double',
             'var': 'var'}

    CLASE_SEPARADOR = {
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
    CLASE_OPERADOR = {
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
    CLASE_BOLEANO = {'tru': 'True',
                'fal': 'False'}

    # Funcion para inicialzar el objeto nodo
    def __init__(self, dato: str):
        self.dato = dato  # Asigna dato
        self.sgte = None  # Inicializa con liga nula

    @property
    def clase(self):
        if re.search(pattern=f"^({'|'.join(self.CLASE_TIPO.values())})$", string=self.dato):
            return 'tip'
        elif re.search(pattern=f"^({'|'.join(self.CLASE_SEPARADOR.values())})$", string=self.dato):
            return 'sep'
        elif re.search(pattern=f"^({'|'.join(self.CLASE_OPERADOR.values())})$", string=self.dato):
            return 'opr'
        elif re.search(pattern=f"^({'|'.join(self.CLASE_BOLEANO.values())})$", string=self.dato):
            return 'bol'
        elif re.search(pattern=f"^[a-zA-Z][a-zA-Z0-9_.]*$", string=self.dato):
            return 'var'
        elif re.search(pattern=f"(^[+-]?[0-9]*[.]?[0-9]*[e]?[+-]?[0-9]$|^\".*\"$)", string=self.dato):
            return 'con'
        else:
            return 'err'

    @property
    def simbolo(self):
        if re.search(pattern=f"^({'|'.join(self.SIMBOLOS_TIPO.values())})$", string=self.dato):
            return 'tip'
        elif re.search(pattern=f"^({'|'.join(self.SIMBOLOS_COMA.values())})$", string=self.dato):
            return 'com'
        elif re.search(pattern=f"^({'|'.join(self.SIMBOLOS_IGUAL.values())})$", string=self.dato):
            return 'igu'
        elif re.search(pattern=f"^({'|'.join(self.SIMBOLOS_BOLEANO.values())})$", string=self.dato):
            return 'bol'
        elif re.search(pattern=f"^({'|'.join(self.SIMBOLOS_SEPARADOR.values())})$", string=self.dato):
            return 'sep'
        elif re.search(pattern=f"^({'|'.join(self.SIMBOLOS_MATEMATICO.values())})$", string=self.dato):
            return 'opr'
        elif re.search(pattern=f"^({'|'.join(self.SIMBOLOS_ASIGNAR.values())})$", string=self.dato):
            return 'asi'
        elif re.search(pattern=f"^({'|'.join(self.SIMBOLOS_LOGICO.values())})$", string=self.dato):
            return 'log'
        elif re.search(pattern=f"^({'|'.join(self.SIMBOLOS_PUNTOYCOMA.values())})$", string=self.dato):
            return 'pyc'
        elif re.search(pattern=f"^({'|'.join(self.SIMBOLOS_DOSPUNTOS.values())})$", string=self.dato):
            return 'dpt'
        elif re.search(pattern=f"^({'|'.join(self.SIMBOLOS_NEGACION.values())})$", string=self.dato):
            return 'neg'
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
