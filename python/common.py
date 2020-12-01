import time


def read_file(file_name):
    with open(f'input/{file_name}.txt') as f:
        lines = f.readlines()
    return [l.strip() for l in lines]


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'{elapsed_time * 1000:.2f} ms')
        print()
        return result
    return wrapper
