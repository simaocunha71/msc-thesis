        if(n == 1) return x > 0;
        if(x == 1) return true;
        while(x % n == 0) {
            x /= n;
        }
        return x == 1;
    }

public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.isSimplePower(1, 4));
        System.out.println(solution.isSimplePower(2, 2));
        System.out.println(solution.isSimplePower(8, 2));
        System.out.println(solution.isSimplePower(3, 2));
        System.out.println(solution.isSimplePower(3, 1));
        System.out.println(solution.isSimplePower(5, 3));
    }
}
```

The function works by dividing x by n while it is divisible. If it eventually equals 1, then x is a simple power of n. If not, then x is not a simple power of n.

Also, if n equals 1, then any number greater than 0 is a simple power of n. If x equals 1, then it is a simple power of n.

The main function tests the function with various inputs.

This solution has a time complexity of O(log x) because it repeatedly divides x by n until x equals 1.

This solution has a space complexity of O(1) because it only uses a constant amount of space.

Please let me know if you have any questions or if there is anything else you would like to know.

**Note:** This solution assumes that the input will always be valid. You may want to add input validation checks to ensure that the inputs are in the expected range and format.

```java

```

```java

```

```java

```

```java

```

```java

```

```java

```

```java

```

```java

```

```java

```

```java

```

```java

```

```java

```

```java

```

```java

```

