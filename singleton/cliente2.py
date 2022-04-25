from modulo import UNICA_INSTANCIA
import cliente

if __name__ == "__main__":
    print(id(UNICA_INSTANCIA))
    print(id(cliente.UNICA_INSTANCIA))
