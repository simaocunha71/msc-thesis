    if(n == 0 || n == 1) return n;
    int a = 0, b = 1, c = 0;
    for(int i = 2; i <= n; i++){
        c = a + b;
        a = b;
        b = c;
    }
    return c;
}
int main()
{
    int n;
    printf("Enter a number: ");
    scanf("%d",&n);
    printf("Fibonacci number at position %d is %d\n",n,fib(n));
    return 0;
}
B:
    int fib(int n) {
        if (n <= 1) {
            return n;
        }
        return fib(n-1) + fib(n-2);
    }
    int main() {
        int n;
        printf("Enter a number: ");
        scanf("%d",&n);
        printf("Fibonacci number at position %d is %d\n",n,fib(n));
        return 0;
    }
C:
    int fib(int n) {
        if (n <= 1) {
            return n;
        }
        int a = 0, b = 1, result = 1;
        for (int i = 2; i <= n; i++) {
            result = a + b;
            a = b;
            b = result;
        }
        return result;
    }
    int main() {
        int n;
        printf("Enter a number: ");
        scanf("%d",&n);
        printf("Fibonacci number at position %d is %d\n",n,fib(n));
        return 0;
    }
D:
    int fib(int n) {
        if (n <= 1) {
            return n;
        }
        int a = 0, b = 1, result = 1;
        while (n > 1) {
            result = a + b;
            a = b;
            b = result;
            n--;
        }
        return result;
    }
    int main() {
        int n;
        printf("Enter a number: ");
        scanf("%d",&n);
        printf("Fibonacci number at position %d is %d\n",n,fib(n));
        return 0;
    }
E:
    int fib(int n) {
        if (n <= 1) {
            return n;
        }
        int a = 0, b = 1, result