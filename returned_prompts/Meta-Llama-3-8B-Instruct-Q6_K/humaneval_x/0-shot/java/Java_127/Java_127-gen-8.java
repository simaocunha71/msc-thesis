Here is the Java solution for the problem:

```java
public String intersection(List<Integer> interval1, List<Integer> interval2) {
    int start1 = Math.max(interval1.get(0), interval2.get(0));
    int end1 = Math.min(interval1.get(1), interval2.get(1));
    if (start1 > end1) {
        return "NO";
    }
    int length = end1 - start1 + 1;
    for (int i = 2; i <= Math.sqrt(length); i++) {
        if (length % i == 0) {
            return "NO";
        }
    }
    return "YES";
}
```

This solution first calculates the intersection of the two intervals by taking the maximum of the start points and the minimum of the end points. If the intersection is empty, it returns "NO". Then it checks whether the length of the intersection is a prime number by iterating from 2 to the square root of the length and checking if the length is divisible by any of these numbers. If the length is divisible, it returns "NO". Otherwise, it returns "YES".