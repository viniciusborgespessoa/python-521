def zero_division_to_inf(fn):
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except ZeroDivisionError:
            return float('inf')
    return wrapper

@zero_division_to_inf
def f(x):
    return 1 / x

@zero_division_to_inf
def g(x, y, z):
    return x ** y * (z / x)

@zero_division_to_inf
def h(x):
    return 99 / (x - 3)

v = [ 'Lucas', 'Ricciardi', 'de', 'Salles' ]

inf = float('inf') 

X = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

for x in X:
    print('f({}) = {}'.format(x, g(x, 2, 2)))

def cache(fn):
    fn._cache = {}
    def wrapper(*args, **kwargs):
        if args not in fn._cache:
            fn._cache[args] = fn(*args)
        return fn._cache[args]
    return wrapper

def fib(n):
    if n < 1:
        return 1
    return fib(n-1) + fib(n-2)

fib = cache(fib)

for i in range(100):
    print(i, fib(i))

def login_required(fn):
    def wrapper(*args, **kwargs):
        user = User.get_by_email(flask.request.cookies.get('email'))
        if not user.authenticated():
            return 'permission denied', 403
        return fn(*args, **kwargs)
    return wrapper