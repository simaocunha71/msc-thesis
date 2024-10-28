```java
public int fib4(int n) {
    if (n < 2) {
        return 0;
    } else if (n == 2) {
        return 2;
    } else {
        int a = 0;
        int b = 0;
        int c = 2;
        int d = 0;
        for (int i = 3; i <= n; i++) {
            int temp = a + b + c + d;
            a = b;
            b = c;
            c = d;
            d = temp;
        }
        return d;
    }
}
```