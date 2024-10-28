        List<Object> result = new ArrayList<>();

        StringBuilder builder = new StringBuilder(s);
        for (char cc : c.toCharArray()) {
            while (builder.indexOf(cc) >= 0) {
                builder.deleteCharAt(builder.indexOf(cc));
            }
        }
        result.add(builder.toString());
        result.add(isPalindrome(builder.toString()));
        return result;
    }

    private boolean isPalindrome(String s) {
        for (int i = 0; i < s.length() / 2; i++) {
            if (s.charAt(i) != s.charAt(s.length() - 1 - i)) {
                return false;
            }
        }
        return true;
    }
}


public class JavaApplication7 {

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.reverseDelete("abcdedcba", "ab"));
    }

}
```