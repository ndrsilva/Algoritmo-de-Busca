"""..."""
import time

def time_statistics(func):
    """..."""
    
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f'Tempo de execução: {end - start}')
        return result

    return wrapper