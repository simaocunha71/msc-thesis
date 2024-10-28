Here is a Java solution using the given problem description:

```java
public String intersection(List<Integer> interval1, List<Integer> interval2) {
    int start1 = Math.max(interval1.get(0), interval2.get(0));
    int end1 = Math.min(interval1.get(1), interval2.get(1));

    if (start1 > end1) {
        return "NO";
    }

    int length = end1 - start1 + 1;
    if (isPrime(length)) {
        return "YES";
    } else {
        return "NO";
    }
}

public boolean isPrime(int num) {
    if (num <= 1) {
        return false;
    }
    for (int i = 2; i <= Math.sqrt(num); i++) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}
```

This solution first calculates the start and end of the intersection of the two intervals. If the start is greater than the end, it means the intervals don't intersect, so it returns "NO". Otherwise, it calculates the length of the intersection. If the length is a prime number, it returns "YES", otherwise it returns "NO". The `isPrime` function checks if a number is prime. It returns `false` if the number is less than or equal to 1, and `true` if the number is greater than 1 and has no divisors other than 1 and itself. It checks divisibility up to the square root of the number.