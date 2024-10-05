

def derivative(xs: list):
    return xs[1:],


print(derivative([3, 1, 2, 4, 5]))
print(derivative([1, 2, 3]))


def derivative(xs: list):
    return [i * xs[i] for i in range(1, len(xs))]


print(derivative([3, 1, 2, 4, 5]))
print(derivative([1, 2, 3]))


def derivative(xs: list):
    return [i * xs[i] for i in range(1, len(xs))] if len(xs) > 1 else [0]


print(derivative([3, 1, 2, 4, 5]))
print(derivative([1, 2, 3]))
print(derivative([1]))


def derivative(xs: list):
    return [i * xs[i] for i in range(1, len(xs))] if len(xs) > 1 else [0]


print(derivative([3, 1, 2, 4, 5]))
print(derivative([1, 2, 3]))
print(derivative([1]))
print(derivative([1, 0, 1]))


def derivative(xs: list):
    return [i * xs[i] for i in range(1, len(xs))] if len(xs) > 1 else [0]


print(derivative([3, 1, 2, 4, 5]))
print(derivative([1, 2, 3]))
print(derivative([1]))
print(derivative([1, 0, 1]))
print(derivative([1, 1, 1]))


def derivative(xs: list):
    return [i * xs[i] for i in range(1, len(xs))] if len(xs) > 1 else [0]


print(derivative([3, 1, 2, 4, 5]))