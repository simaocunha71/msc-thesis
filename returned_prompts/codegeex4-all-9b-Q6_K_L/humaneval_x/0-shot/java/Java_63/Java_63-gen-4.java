Here is a java solution for the problem:

```java
public int fibfib(int n) {
    int[] fibfib = new int[n+1];
    if(n == 0) return 0;
    if(n == 1) return 0;
    if(n == 2) return 1;

    fibfib[0] = 0;
    fibfib[1] = 0;
    fibfib[2] = 1;

    for(int i = 3; i <= n; i++){
        fibfib[i] = fibfib[i-1] + fibfib[i-2] + fibfib[i-3];
    }
    return fibfib[n];
}
```
The solution first checks for the base cases where n is 0, 1 or 2. It then initializes the first three elements of the fibfib array with 0, 0 and 1. It then enters a loop from 3 to n and calculates the ith element as the sum of the (i-1)th, (i-2)th and (i-3)th elements. At the end of the loop, it returns the nth element of the fibfib array. This solution has a time complexity of O(n) and a space complexity of O(n).