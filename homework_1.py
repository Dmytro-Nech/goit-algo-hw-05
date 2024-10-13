def caching_fibonacci():
    # створюємо словник для кеша
    cache = {}
    def fibonacci(n):
        # перевіряємо всі умови
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci (n -2)
            return cache[n]
    # повертаємо внутрішню функцію
    return fibonacci

def main():
    fib = caching_fibonacci()
    print(fib(10))
    print(fib(15))

if __name__ == "__main__":
    main()