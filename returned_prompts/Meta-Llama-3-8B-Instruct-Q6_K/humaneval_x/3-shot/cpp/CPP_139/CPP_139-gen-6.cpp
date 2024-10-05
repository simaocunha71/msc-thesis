    long long result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i;
        for (int j = i - 1; j >= 1; j--) {
            result *= j;
        }
    }
    return result;
}  // This solution is incorrect because it doesn't correctly calculate the Brazilian factorial.


