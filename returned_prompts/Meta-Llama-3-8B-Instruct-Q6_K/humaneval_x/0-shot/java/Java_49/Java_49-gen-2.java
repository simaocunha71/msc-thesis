public int modp(int n, int p) {
    if (n == 0) {
        return 1;
    }
    if (n % 2 == 0) {
        int half = modp(n / 2, p);
        return (half * half) % p;
    } else {
        int half = modp(n / 2, p);
        return ((half * half) % p * 2) % p;
    }
}