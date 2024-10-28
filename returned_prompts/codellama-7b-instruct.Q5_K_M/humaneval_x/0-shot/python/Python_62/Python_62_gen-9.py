

def derivative(xs: list):
    result = [0] * (len(xs) - 1)
    for i in range(1, len(result)):
        result[i] = i * xs[i]
    return result
