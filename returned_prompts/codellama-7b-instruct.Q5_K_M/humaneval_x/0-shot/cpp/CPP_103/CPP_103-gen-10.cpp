    if (n > m) {
        return "-1";
    }
    int sum = 0;
    for (int i = n; i <= m; i++) {
        sum += i;
    }
    int avg = sum / (m - n + 1);
    int avg_round = (int)round(avg);
    int binary[10] = { 0 };
    int j = 0;
    while (avg_round > 0) {
        binary[j] = avg_round % 2;
        j++;
        avg_round /= 2;
    }
    string str = "";
    for (int k = j - 1; k >= 0; k--) {
        str += to_string(binary[k]);
    }
    return str;
}
int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    printf("%s\n", rounded_avg(n, m).c_str());
    return 0;
}
