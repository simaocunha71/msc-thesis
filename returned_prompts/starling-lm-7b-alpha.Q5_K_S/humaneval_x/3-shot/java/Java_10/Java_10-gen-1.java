        StringBuilder string_builder = new StringBuilder(string);
        int i = string.length() - 1;
        while (!isPalindrome(string_builder.substring(0, i + 1))) {
            i--;
        }
        String postfix = string_builder.substring(string.length() - i, string.length());
        String prefix = string_builder.substring(0, string.length() - i);
        return string_builder.toString() + reverse(prefix);
    }

    public String reverse(String string) {
        StringBuilder string_builder = new StringBuilder(string);
        Collections.reverse(string_builder);
        return string_builder.toString();
    }
}


public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5);
        solution.separateParenGroups("( ) (( )) (( )( ))");
        solution.truncateNumber(3.5);
        solution.isPalindrome("civic");
        solution.makePalindrome("civic");
    }
}
```