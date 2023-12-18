"""..."""
from time_statistcs import time_statistics


@time_statistics
def busca_linear(lista, item_pesquisado):
    """..."""

    tamanho_da_lista = len(lista)
    for atual in range(0, tamanho_da_lista):
        if (lista[atual] == item_pesquisado):
            return atual

    return -1