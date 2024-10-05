```java
public Object roundedAvg(int n, int m) {
    if (n > m) return -1;
    int sum = 0;
    int count = 0;
    for (int i = n; i <= m; i++) {
        sum += i;
        count++;
    }
    int avg = Math.round((float) sum / count);
    String binary = Integer.toBinaryString(avg);
    return binary;
}
```