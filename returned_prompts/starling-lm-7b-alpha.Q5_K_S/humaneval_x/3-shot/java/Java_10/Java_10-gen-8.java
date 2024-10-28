        String palindromic_suffix = palindromicSuffix(string);
        StringBuilder result = new StringBuilder(string);
        result.append(palindromicSuffix);
        result.insert(0, reverseString(result.substring(0, palindromicSuffix.length())));
        return result.toString();
    }

    private String reverseString(String s) {
        return new StringBuilder(s).reverse().toString();
    }

    private String palindromicSuffix(String s) {
        int length = s.length();
        for (int i = length - 2; i >= 0; i--) {
            if (s.charAt(i) == s.charAt(length - 1)) {
                String suffix = s.substring(i, length);
                if (isPalindrome(suffix)) {
                    return suffix;
                }
            }
        }
        return "";
    }
}


public class _2020_01_28_solutions {

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.isPalindrome(""));
        System.out.println(solution.makePalindrome(""));
        System.out.println(solution.makePalindrome("cat"));
        System.out.println(solution.makePalindrome("cata"));
    }

}

```