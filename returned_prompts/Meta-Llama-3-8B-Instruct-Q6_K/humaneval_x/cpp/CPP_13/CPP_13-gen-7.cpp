    if (b == 0) {
        return a;
    }
    return greatest_common_divisor(b, a % b);
}
int main() {
    printf("%d\n", greatest_common_divisor(25, 15));
    return 0;
}

S:
The function `greatest_common_divisor` takes two integers `a` and `b` as input and returns their greatest common divisor (GCD). The function uses the Euclidean algorithm, which is an efficient method for computing the GCD of two numbers.

The function works by repeatedly replacing `a` and `b` with `b` and the remainder of `a` divided by `b`, respectively, until `b` is zero. At that point, `a` is the GCD of the original `a` and `b`.

In the `main` function, we call `greatest_common_divisor` with the arguments `25` and `15`, and print the result using `printf`. The output is `5`, which is the GCD of `25` and `15`.