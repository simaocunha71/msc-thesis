public int modp(int n, int p) {
    if(n == 0) return 1;
    if(n == 1) return n % p;
    int res = modp(n/2, p);
    if(n % 2 == 0) {
        return (res * res) % p;
    } else {
        return ((res * res) % p * n) % p;
    }
}