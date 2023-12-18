"""..."""
from time_statistcs import time_statistics


@time_statistics
def busca_binaria_iterativa(lista, item_pesquisado):
    """..."""

    inicio = 0
    fim = len(lista) - 1

    while inicio<=fim:
        meio = (inicio + fim) // 2

        if lista[meio] == item_pesquisado:
            return meio
        
        elif lista[meio] < item_pesquisado:
            inicio = meio + 1

        elif lista[meio] > item_pesquisado:
            fim = meio - 1

    return -1

@time_statistics
def busca_binaria_recursiva(lista, item_pesquisado, inicio=0, fim=None):
    """..."""

    if fim is None:
        fim = len(lista) - 1

    if inicio > fim:
        return -1

    meio = (inicio + fim) // 2

    if lista[meio] == item_pesquisado:
        return meio

    elif lista[meio] < item_pesquisado:
        return busca_binaria_recursiva(lista, item_pesquisado, meio + 1, fim)

    else:
        return busca_binaria_recursiva(lista, item_pesquisado, inicio, meio - 1)
