public boolean isSimplePower(int x, int n) {
    double res = Math.log(x) / Math.log(n);
    return res == Math.floor(res);
}