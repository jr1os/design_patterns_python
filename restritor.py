
class Cao:
    def __init__(self, nome, raca, sexo):
        self._sexo = sexo
        self.nome = nome
        self.raca = raca

    def latir(self):
        return 'Au'


class EmbrulhoRestritor:
    def __init__(self, embrulhado):
        self._embrulhado = embrulhado

    def __getattr__(self, nome):
        if nome.startswith("_"):
            raise AttributeError("nao e possivel acessar atributo")
        return getattr(self._embrulhado, nome)


if __name__ == "__main__":
    rex = Cao('Rex', 'vira lata', 'Macho')
    print(rex.nome, rex.raca, rex._sexo)

    rex_restrito = EmbrulhoRestritor(rex)
    print(rex.__dict__)
    print(rex_restrito.latir())
    print(rex_restrito.nome)
    print(rex_restrito._sexo)

    # fiona = Cao('Fiona', 'Beagle', 'femea')
