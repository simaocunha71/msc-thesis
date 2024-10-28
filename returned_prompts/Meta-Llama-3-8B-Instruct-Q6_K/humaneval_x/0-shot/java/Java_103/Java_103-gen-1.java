public Object roundedAvg(int n, int m) {
    if (n > m) {
        return -1;
    }
    int sum = 0;
    for (int i = n; i <= m; i++) {
        sum += i;
    }
    double average = (double) sum / (m - n + 1);
    double rounded = Math.round(average);
    return Integer.toBinaryString((int) rounded);
}