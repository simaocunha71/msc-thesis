    if (b == 0) {
        return a;
    } else {
        return greatest_common_divisor(b, a % b);
    }
}

int main() {
    int a = 3;
    int b = 5;
    printf("%d\n", greatest_common_divisor(a, b));
    return 0;
}
