    vector<int> result;
    while (n != 1) {
        if (n % 2 == 0) {
            n = n / 2;
        } else {
            n = 3 * n + 1;
        }
    }
    while (n != 0) {
        if (n % 2 != 0) {
            result.push_back(n);
            n = n / 2;
        } else {
            n = n / 2;
        }
    }
    sort(result.begin(), result.end());
    return result;
}
int main() {
    printf("%lu\n", get_odd_collatz(5).size());
    for (int i = 0; i < get_odd_collatz(5).size(); i++) {
        printf("%d ", get_odd_collatz(5)[i]);
    }
    return 0;
}
