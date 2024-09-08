    if(b==0) return a;
    else return greatest_common_divisor(b, a%b);
}
int main() {
    printf("%d\n", greatest_common_divisor(3, 5));
    printf("%d\n", greatest_common_divisor(25, 15));
    return 0;
}
B:
    int gcd(int a, int b) {
        if (b == 0) {
            return a;
        } else {
            return gcd(b, a % b);
        }
    }
    int main() {
        printf("%d\n", gcd(3, 5));
        printf("%d\n", gcd(25, 15));
        return 0;
    }
C:
    int gcd(int a, int b) {
        if (b == 0) {
            return a;
        } else {
            return gcd(b, a % b);
        }
    }
    int main() {
        printf("%d\n", gcd(3, 5));
        printf("%d\n", gcd(25, 15));
        return 0;
    }
D:
    int gcd(int a, int b) {
        if (b == 0) {
            return a;
        } else {
            return gcd(b, a % b);
        }
    }
    int main() {
        printf("%d\n", gcd(3, 5));
        printf("%d\n", gcd(25, 15));
        return 0;
    }
E:
    int gcd(int a, int b) {
        if (b == 0) {
            return a;
        } else {
            return gcd(b, a % b);
        }
    }
    int main() {
        printf("%d\n", gcd(3, 5));
        printf("%d\n", gcd(25, 15));
        return 0;
    }
F:
    int gcd(int a, int b) {
        if (b == 0) {
            return a;
        } else {
            return gcd(b, a % b);
        }
    }
    int main() {
        printf("%d\n", gcd(3, 5));
        printf("%d\n", gcd(25, 15));
        return 0;
    }
G:
    int gcd(int a, int b) {
        if (b == 0) {
            return a;
        } else {
            return gcd(b, a % b);
        }
    }
    int main() {
