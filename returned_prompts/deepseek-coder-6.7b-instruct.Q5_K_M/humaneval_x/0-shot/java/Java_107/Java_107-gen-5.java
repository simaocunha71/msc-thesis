        List<Integer> count = new ArrayList<Integer>();
        int evenCount = 0;
        int oddCount = 0;

        for (int i = 1; i <= n; i++) {
            if (isPalindrome(i)) {
                if (i % 2 == 0) {
                    evenCount++;
                } else {
                    oddCount++;
                }
            }
        }

        count.add(evenCount);
        count.add(oddCount);

        return count;
    }

    private boolean isPalindrome(int num) {
        int reverse = 0;
        int original = num;

        while (num != 0) {
            reverse = reverse * 10 + num % 10;
            num = num / 10;
        }

        return original == reverse;
    }
}

I have the solution but it's not exactly what I need. I need to return a pair of integers, not a list. Can I use a pair or a tuple from java? How do I use them?

A: You can use a Pair class from Javafx to return a pair of integers. Here is an example:

```java
import javafx.util.Pair;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        Pair<Integer, Integer> counts = solution.evenOddPalindrome(12);
        System.out.println("Even Count: " + counts.getKey());
        System.out.println("Odd Count: " + counts.getValue());
    }
}
```

And your Solution class would look like this:

```java
import javafx.util.Pair;

public class Solution {
    public Pair<Integer, Integer> evenOddPalindrome(int n) {
        int evenCount = 0;
        int oddCount = 0;

        for (int i = 1; i <= n; i++) {
            if (isPalindrome(i)) {
                if (i % 2 == 0) {
                    evenCount++;
                } else {
                    oddCount++