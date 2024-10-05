        if (b == 0) return a;
        return greatestCommonDivisor(b, a % b);
    }
}

This algorithm uses the Euclidean algorithm to find the greatest common divisor of two numbers. It works by continually replacing 'a' with 'b' and 'b' with 'a mod b' until 'b' equals 0. At that point, 'a' is the greatest common divisor.
*/

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.greatestCommonDivisor(3, 5)); // 1
        System.out.println(solution.greatestCommonDivisor(25, 15)); // 5
    }
}
```

## Binary Search

```java
/*
