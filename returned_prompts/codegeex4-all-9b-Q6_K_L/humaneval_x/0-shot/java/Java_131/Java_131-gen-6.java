The given problem is a straightforward one. We need to extract the digits of the given number and check if they are odd or even. If the digit is odd, we multiply it to a variable and return it in the end. If all digits are even, we return 0.

Here is the Java code to solve the problem:

```java
public class Solution {
    public static int digits(int n) {
        int product = 1;
        boolean allEven = true;

        while (n > 0) {
            int digit = n % 10;
            if (digit % 2 != 0) {
                product *= digit;
                allEven = false;
            }
            n /= 10;
        }

        return allEven ? 0 : product;
    }

    public static void main(String[] args) {
        System.out.println(digits(1));  // Output: 1
        System.out.println(digits(4));  // Output: 0
        System.out.println(digits(235)); // Output: 15
    }
}
```

In this code, we use a while loop to extract the digits of the given number. We check if the digit is odd by using the modulus operator. If the digit is odd, we multiply it to the product variable. If all digits are even, we set the allEven flag to false. Finally, we return the product if all digits are odd, otherwise we return 0.