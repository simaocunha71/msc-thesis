```java
import java.util.*;

public class Solution {
    public List<Integer> evenOddPalindrome(int n) {
        int even = 0, odd = 0;
        for (int i = 1; i <= n; i++) {
            if (isPalindrome(i) && i % 2 == 0) {
                even++;
            } else if (isPalindrome(i) && i % 2 != 0) {
                odd++;
            }
        }
        List<Integer> result = new ArrayList<>();
        result.add(even);
        result.add(odd);
        return result;
    }

    public boolean isPalindrome(int num) {
        int temp = num, reversed = 0;
        while (temp != 0) {
            int remainder = temp % 10;
            reversed = reversed * 10 + remainder;
            temp /= 10;
        }
        return num == reversed;
    }
}
```
This Java solution defines a method `evenOddPalindrome` that takes an integer `n` as input and returns a list of two integers representing the count of even and odd integer palindromes within the range (1, n), inclusive.

The method iterates through the range (1, n) using a for loop and checks each integer for being a palindrome and even or odd using the `isPalindrome` method. If the integer is a palindrome and even, it increments the `even` counter; if it's a palindrome and odd, it increments the `odd` counter.

The `isPalindrome` method checks if a given integer is a palindrome by reversing the integer and comparing it with the original integer.

Finally, the method returns a list containing the `even` and `odd` counters as elements. The list is created using the `ArrayList` class. The solution is efficient, with a time complexity of O(n log n) due to the `isPalindrome` method and a space complexity of O(1) since it only uses a constant amount of space.