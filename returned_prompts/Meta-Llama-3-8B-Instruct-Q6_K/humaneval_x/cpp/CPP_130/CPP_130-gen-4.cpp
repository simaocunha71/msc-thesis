    vector<int> result(n + 1);
    result[0] = 1;
    result[1] = 3;
    if (n >= 2) {
        result[2] = 1 + 2 / 2;
    }
    for (int i = 3; i <= n; i++) {
        if (i % 2 == 0) {
            result[i] = 1 + i / 2;
        } else {
            result[i] = result[i - 1] + result[i - 2] + result[i + 1];
        }
    }
    return result;
}

int main() {
    printf("%d, %d, %d, %d\n", tri(3)[0], tri(3)[1], tri(3)[2], tri(3)[3]);
    return 0;
}
