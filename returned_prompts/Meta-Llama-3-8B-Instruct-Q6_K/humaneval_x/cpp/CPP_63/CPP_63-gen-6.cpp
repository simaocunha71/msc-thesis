    if(n <= 1){
        return 0;
    }
    else if(n == 2){
        return 1;
    }
    else{
        int a = 0, b = 0, c = 1;
        for(int i = 3; i <= n; i++){
            int temp = a + b + c;
            a = b;
            b = c;
            c = temp;
        }
        return c;
    }
}
int main() {
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    printf("FibFib number at position %d is %d\n", n, fibfib(n));
    return 0;
}
B:
    int fibfib(int n) {
        if (n <= 1) {
            return 0;
        } else if (n == 2) {
            return 1;
        } else {
            int a = 0, b = 0, c = 1;
            int i = 3;
            while (i <= n) {
                int temp = a + b + c;
                a = b;
                b = c;
                c = temp;
                i++;
            }
            return c;
        }
    }

    int main() {
        int n;
        printf("Enter the value of n: ");
        scanf("%d", &n);
        printf("FibFib number at position %d is %d\n", n, fibfib(n));
        return 0;
    }
C:
    int fibfib(int n) {
        if (n <= 1) {
            return 0;
        } else if (n == 2) {
            return 1;
        } else {
            int a = 0, b = 0, c = 1;
            for (int i = 3; i <= n; i++) {
                int temp = a + b + c;
                a = b;
                b = c;
                c = temp;
            }
            return c;
        }
    }

    int main() {
        int n;
        printf("Enter the value of n: ");
        scanf("%d", &n);
        printf("FibFib number at position %d is %d\n", n, fibfib(n));
        return 0;
    }
D:
    int fibfib(int n) {
        if (n <= 1) {
           