    public List<Integer> evenOddPalindrome(int n) {
        int even = 0, odd = 0;
        for (int i = 1; i <= n; i++) {
            String s = Integer.toString(i);
            if (isPalindrome(s)) {
                if (isEven(i)) {
                    even++;
                } else {
                    odd++;
                }
            }
        }
        return Arrays.asList(even, odd);
    }

    private boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    private boolean isEven(int num) {
        return num % 2 == 0;
    }
}

Explanation:

The problem asks to count the number of even and odd integer palindromes within a given range. We solve this by iterating over the range and checking each number for palindromity and parity.

The helper method `isPalindrome` checks if a given string is a palindrome by comparing characters from both ends. The method `isEven` checks if a number is even by checking its remainder when divided by 2.

In the main method, we iterate over the range and for each number, we convert it to a string, check if it's a palindrome using `isPalindrome`, and then check its parity using `isEven`. If it's a palindrome and even, we increment the `even` count; if it's a palindrome and odd, we increment the `odd` count.

Finally, we return a list containing the counts of even and odd integer palindromes. The unit tests provided help to clarify the problem and ensure the correctness of the solution.