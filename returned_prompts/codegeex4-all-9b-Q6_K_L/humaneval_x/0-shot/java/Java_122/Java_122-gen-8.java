```java
public int addElements(List<Integer> arr, int k) {
    int sum = 0;
    for (int i = 0; i < k; i++) {
        int num = arr.get(i);
        int digits = 0;
        while (num > 0) {
            num /= 10;
            digits++;
        }
        if (digits <= 2) {
            sum += arr.get(i);
        }
    }
    return sum;
}
```