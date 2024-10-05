        String suffix = string.substring(string.length() - 1);
        while (!isPalindrome(suffix)) {
            suffix = string.substring(string.length() - suffix.length());
        }
        return suffix;
    }

    /**
    Reverse the string
    >>> reverseString("cat")
    "tac"
    >>> reverseString("")
    ""
     */
    public String reverseString(String string) {
        StringBuilder result = new StringBuilder();
        for (int i = string.length() - 1; i >= 0; i--) {
            result.append(string.charAt(i));
        }
        return result.toString();
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.makePalindrome("cab"));
    }
}

```