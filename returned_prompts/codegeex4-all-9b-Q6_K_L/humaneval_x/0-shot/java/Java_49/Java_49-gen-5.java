```java
public int modp(int n, int p) {
    if (n == 0) return 1;
    int half = modp(n / 2, p);
    if (n % 2 == 0) return (half * half) % p;
    else return (half * half * 3) % p;
}
```