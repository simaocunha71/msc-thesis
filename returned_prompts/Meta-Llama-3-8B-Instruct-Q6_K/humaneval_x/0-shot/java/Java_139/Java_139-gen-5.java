public long specialFactorial(int n) {
    long res = 1;
    for(int i = 1; i <= n; i++) {
        res *= i;
        if(i > 1) {
            for(int j = 2; j <= i; j++) {
                res *= j;
            }
        }
    }
    return res;
}