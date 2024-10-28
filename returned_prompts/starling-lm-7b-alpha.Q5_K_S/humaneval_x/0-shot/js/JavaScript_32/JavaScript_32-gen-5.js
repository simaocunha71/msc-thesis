To find zero point for a polynomial, we can use Newton's method. Newton's method uses derivative of a function to find a zero point of it.

First, we need to find a derivative of a polynomial. Here is a Python code to do that:
```python
def poly_derivative(xs):
    derivatives = []
    for i in range(len(xs)):
        if i == 0:
            derivatives.append(xs[i+1])
        else:
            derivatives.append(xs[i+1] * i)
    return derivatives
```

Next, we need to find a zero point of a function. Here is a Python code to do that:
```python
def newton_method(f, f_prime, x, epsilon=10**-12):
    while abs(f(x)) > epsilon:
        x = x - f(x) / f_prime(x)
    return x
```

Finally, we can find a zero point of a polynomial with given coefficients. Here is a Python code to do that:
```python
def find_zero(xs):
    derivatives = poly_derivative(xs)
    f = lambda x: poly(xs, x)
    f_prime = lambda x: poly(derivatives, x)
    return newton_method(f, f_prime, 1)
```

You can use above Python code to find a zero point of a polynomial. Note that the Newton's method may not work well if the function is not smooth.

As for JavaScript, you can use the same logic to find a zero point of a polynomial. Here is a JavaScript code to do that:
```javascript
function poly_derivative(xs) {
    var derivatives = [];
    for (var i = 0; i < xs.length; i++) {
        if (i == 0) {
            derivatives.push(xs[i+1]);
        } else {
            derivatives.push(xs[i+1] * i);
        }
    }
    return derivatives;
}

function newton_method(f, f_prime, x, epsilon=