"""..."""
from time_statistcs import time_statistics
from busca_linear import busca_linear
from busca_binaria import busca_binaria_iterativa
from busca_binaria import busca_binaria_recursiva


@time_statistics
def gerar_lista_numeros(de: int, ate: int):
    """..."""

    return list(range(de, ate))


if __name__ == '__main__':
    print('Gerando a lista de Números.')
    lista_numeros = gerar_lista_numeros(de=1, ate=1000000000)
    print('')

    print('Busca Binária Iterativa.')
    busca_binaria_iterativa_ = busca_binaria_iterativa(lista_numeros, 9999999)
    print(f'Resultado: {busca_binaria_iterativa_}\n')

    print('Busca Binária Recursiva.')
    busca_binaria_recursiva_ = busca_binaria_recursiva(lista_numeros, 9999999)
    print(f'Resultado: {busca_binaria_recursiva_}\n')

    print('Busca Linear.')
    busca_linear_ = busca_linear(lista_numeros, 9999999)
    print(f'Resultado: {busca_linear_}\n')