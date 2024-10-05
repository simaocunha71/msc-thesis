        List<Object> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();

        for (char ch : s.toCharArray()) {
            if (!c.contains(String.valueOf(ch))) {
                sb.append(ch);
            }
        }

        String rev = sb.toString();
        String org = new StringBuilder(rev).reverse().toString();
        result.add(org.equals(rev) ? org : rev);
        result.add(org.equals(rev));

        return result;
    }
}


A: Your code is almost correct. The main thing is that you need to check if the resultant string is palindrome after deleting the characters from string s.
You can reverse the string and then check if both strings are equal or not. If both are equal then the string is palindrome, else it is not.
Here is the correct code:
import java.util.*;

class Solution {
    public List<Object> reverseDelete(String s, String c) {
        List<Object> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();

        for (char ch : s.toCharArray()) {
            if (!c.contains(String.valueOf(ch))) {
                sb.append(ch);
            }
        }

        String rev = sb.toString();
        String org = new StringBuilder(rev).reverse().toString();
        result.add(org.equals(rev) ? org : rev);
        result.add(org.equals(rev));

        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.reverseDelete("abcde", "ae")); // output: [bcd, false]
        System.out.println(sol.reverseDelete("abcdef", "b")); // output: [acdef, false]
        System.out.println(sol.reverseDelete("abcdedcba", "ab")); // output: [cdedc, true]
    }
}

In the main method, I'm calling reverseDelete method with different inputs and printing the results.
