Here is a solution in Java:

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(startsOneEnds(2)); // Output: 9
        System.out.println(startsOneEnds(3)); // Output: 99
        System.out.println(startsOneEnds(4)); // Output: 999
    }

    public static int startsOneEnds(int n) {
        // If n is 1, return 1, because 1-digit numbers start and end with 1
        if (n == 1) return 1;

        // Calculate the total count of n-digit numbers
        int totalCount = (int) Math.pow(10, n) - 1;

        // Subtract the count of numbers that do not start or end with 1
        int countNotOne = (int) Math.pow(9, n - 1);

        // Return the count of numbers that start or end with 1
        return totalCount - countNotOne;
    }
}
```

The `startsOneEnds` function calculates the total count of n-digit numbers and subtracts the count of numbers that do not start or end with 1. The count of numbers that do not start or end with 1 is calculated by subtracting 1 from the total count of n-digit numbers and multiplying by 9. This is because for each digit, there are 9 possible numbers (0-9) except for 1.