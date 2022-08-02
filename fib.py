# from rcviz import viz
# from IPython.display import Image
# from functools import lru_cache # deco like memo
import time
import matplotlib.pyplot as plt

# old_fib1 = fib1
# fib1 = viz(fib1)
# fib1(5)
# Image('./fib1.png')


# decorator
def memo(f):
    cache1 = {}

    def inner(n):
        if n not in cache1:
            cache1[n] = f(n)
        return cache1[n]

    return inner


#@memo
def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)


def fib3(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1


def timed(f, *args, n_iter=1000):
    acc = float("inf")
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc


print(fib3(500))
print(timed(fib3, 500))


def compare(fs, args):
    for f in fs:
        plt.plot(args, [timed(f, arg) for arg in args], label=f.__name__)
    plt.legend()
    plt.grid(True)
    plt.show()


compare([fib1, fib3], list(range(20)))
