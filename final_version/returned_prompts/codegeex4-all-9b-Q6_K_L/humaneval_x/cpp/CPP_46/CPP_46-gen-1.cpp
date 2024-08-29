int fib[5] = {0, 0, 2, 0, 0};
    for (int i = 3; i <= n; i++) {
        fib[i % 5] = fib[(i - 1) % 5] + fib[(i - 2) % 5] + fib[(i - 3) % 5] + fib[(i - 4) % 5];
    }
    return fib[n % 5];
}

int main() {
    for (int i = 0; i <= 10; i++) {
        printf("%d\n", fib4(i));
    }
    return 0;
}
B:
int fib4(int n){
    if (n < 2) {
        return 0;
    }
    if (n == 2) {
        return 2;
    }
    int a = 0;
    int b = 0;
    int c = 2;
    int d = 0;
    int result = 0;
    for (int i = 3; i <= n; i++) {
        result = a + b + c + d;
        a = b;
        b = c;
        c = d;
        d = result;
    }
    return result;
}

int main() {
    for (int i = 0; i <= 10; i++) {
        printf("%d\n", fib4(i));
    }
    return 0;
}
C:
int fib4(int n){
    if (n < 2) {
        return 0;
    }
    if (n == 2) {
        return 2;
    }
    int result = 0;
    for (int i = 3; i <= n; i++) {
        result = result + fib4(i - 1) + fib4(i - 2) + fib4(i - 3) + fib4(i - 4);
    }
    return result;
}

int main() {
    for (int i = 0; i <= 10; i++) {
        printf("%d\n", fib4(i));
    }
    return 0;
}
D:
int fib4(int n){
    if (n < 2) {
        return 0;
    }
    if (n == 2) {
        return 2;
    }
    int result = 0;
    for (int i = 3; i