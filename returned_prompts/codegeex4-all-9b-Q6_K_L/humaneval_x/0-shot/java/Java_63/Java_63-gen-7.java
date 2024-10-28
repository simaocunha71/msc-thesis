Here is a Java solution using dynamic programming:

```java
public int fibfib(int n) {
    if (n == 0) return 0;
    if (n == 1) return 0;
    if (n == 2) return 1;
    
    int[] fibfib = new int[n+1];
    fibfib[0] = 0;
    fibfib[1] = 0;
    fibfib[2] = 1;
    
    for (int i = 3; i <= n; i++) {
        fibfib[i] = fibfib[i-1] + fibfib[i-2] + fibfib[i-3];
    }
    
    return fibfib[n];
}
```
In this solution, we first handle the base cases where n is 0, 1 or 2. Then, we create an array to store the fibfib numbers. We initialize the first three numbers in the array, and then use a loop to compute the rest of the fibfib numbers. The i-th fibfib number is computed as the sum of the (i-1)-th, (i-2)-th and (i-3)-th fibfib numbers. Finally, we return the n-th fibfib number.