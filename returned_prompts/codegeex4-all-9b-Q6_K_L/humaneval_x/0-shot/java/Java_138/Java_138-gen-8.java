```java
public boolean isEqualToSumEven(int n) {
    if (n % 2 != 0 || n < 8) {
        return false;
    }
    for (int i = 2; i <= n / 4; i += 2) {
        for (int j = i + 2; j <= n / 3; j += 2) {
            for (int k = j + 2; k <= n / 2; k += 2) {
                int l = n - i - j - k;
                if (l > 0 && l % 2 == 0) {
                    return true;
                }
            }
        }
    }
    return false;
}
```
In this solution, we first check if n is even and greater than or equal to 8. If not, we return false. Then, we iterate over all possible values of i, j, and k that are even numbers and less than or equal to n/4, n/3, and n/2, respectively. For each combination, we calculate l = n - i - j - k. If l is a positive even number, we return true. If no such combination is found, we return false.