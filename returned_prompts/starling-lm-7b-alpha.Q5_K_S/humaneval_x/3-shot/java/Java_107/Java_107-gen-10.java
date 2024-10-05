        int even = 0;
        int odd = 0;

        for (int i = 1; i <= n; i++) {
            if (isPalindrome(i)) {
                if (i % 2 == 0) {
                    even += 1;
                } else {
                    odd += 1;
                }
            }
        }
        return Arrays.asList(even, odd);
    }

    private boolean isPalindrome(int n) {
        int reversed = 0;
        int original = n;
        while (n > 0) {
            reversed *= 10;
            reversed += (n % 10);
            n /= 10;
        }
        return original == reversed;
    }
}


public class Interview {

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.evenOddPalindrome(3));
        System.out.println(solution.evenOddPalindrome(12));
    }
}
```