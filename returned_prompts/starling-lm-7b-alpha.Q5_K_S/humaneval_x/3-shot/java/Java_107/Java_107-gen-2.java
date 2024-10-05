        int even_count = 0;
        int odd_count = 0;
        for (int i = 1; i <= n; i++) {
            String i_str = Integer.toString(i);
            if (isPalindrome(i_str)) {
                if (i % 2 == 0) {
                    even_count += 1;
                } else {
                    odd_count += 1;
                }
            }
        }
        List<Integer> result = new ArrayList<>();
        result.add(even_count);
        result.add(odd_count);
        return result;
    }

    private boolean isPalindrome(String str) {
        int left = 0;
        int right = str.length() - 1;
        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return false;
            }
            left += 1;
            right -= 1;
        }
        return true;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        // sol.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5);
        // sol.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3);
        // sol.separateParenGroups("( ) (( )) (( )( ))");
        // sol.truncateNumber(3.5);
        // sol.evenOddPalindrome(3);
        // sol.evenOddPalindrome(12);
        // System.out.println(sol.evenOddPalindrome(3));
        // System.out.println(sol.evenOddPalindrome(12));
    }
}

```