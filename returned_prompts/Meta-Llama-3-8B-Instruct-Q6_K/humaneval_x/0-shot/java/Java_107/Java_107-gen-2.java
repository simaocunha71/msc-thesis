    public List<Integer> evenOddPalindrome(int n) {
        int even = 0, odd = 0;
        for (int i = 1; i <= n; i++) {
            if (isPalindrome(i) && i % 2 == 0) {
                even++;
            }
            if (isPalindrome(i) && i % 2 != 0) {
                odd++;
            }
        }
        return Arrays.asList(even, odd);
    }

    private boolean isPalindrome(int num) {
        int reversed = 0;
        int original = num;
        while (num != 0) {
            int remainder = num % 10;
            reversed = reversed * 10 + remainder;
            num /= 10;
        }
        return original == reversed;
    }
}
S:
The problem asks to find the number of even and odd integer palindromes within a given range (1, n). A palindrome is a number that remains the same when its digits are reversed. 

The solution is to iterate through the range and check if each number is a palindrome and whether it's even or odd. We use a helper function `isPalindrome` to check if a number is a palindrome. The main function `evenOddPalindrome` initializes two counters, `even` and `odd`, to keep track of the number of even and odd palindromes respectively. For each number in the range, we check if it's a palindrome and if it's even or odd. If it's both, we increment the `even` counter. If it's a palindrome but not even, we increment the `odd` counter. Finally, we return a list containing the counts of even and odd palindromes.

The time complexity of this solution is O(n) because we're iterating through the range once. The space complexity is O(1) because we're using a constant amount of space to store the counters and the list.  S
