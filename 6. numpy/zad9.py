print((lambda n: __import__("numpy").array([[fib(f) for f in range([n * n for _ in [globals().update({"fib":lambda x: 1 if x in (0, 1) else fib(x - 1) + fib(x - 2)}) for __ in range(1)]][0])][i:i + n] for i in range(0, n * n, n)]))(5))