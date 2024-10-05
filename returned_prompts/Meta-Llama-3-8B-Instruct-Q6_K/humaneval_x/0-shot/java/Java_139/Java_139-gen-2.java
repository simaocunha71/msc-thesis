    long result = 1;
    for(int i = 1; i <= n; i++) {
        result *= i;
    }
    for(int i = n; i > 1; i--) {
        result *= specialFactorial(i - 1);
    }
    return result;
}