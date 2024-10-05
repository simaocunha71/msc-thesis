public int solve(int n, int m) {
    if (n > m)
        return -1;
    int count = 0, sum = 0;
    for (int i = n; i <= m; i++) {
        count++;
        sum += i;
    }
    double avg = sum / count;
    int r = (int) Math.round(avg);
    return Integer.toBinaryString(r);
}

