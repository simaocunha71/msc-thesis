public long specialFactorial(int n) {
    long result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i * specialFactorial(i - 1);
    }
    return result;
}