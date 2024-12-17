import functools


def is_prime(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        for i in range(2, value // 2 + 1):
            if value % i == 0:
                print(f'Составное')
                break
        else:
            print('Простое')
        return value
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 2)
print(result)
