Here is a Java solution using a HashSet to store the characters in the string c, then iterate over the string s to remove the characters that are in the set. Finally, check if the resulting string is a palindrome.

```java
import java.util.*;

class Solution {
    public List<Object> reverseDelete(String s, String c) {
        Set<Character> set = new HashSet<>();
        for (char ch : c.toCharArray()) {
            set.add(ch);
        }

        StringBuilder sb = new StringBuilder();
        for (char ch : s.toCharArray()) {
            if (!set.contains(ch)) {
                sb.append(ch);
            }
        }

        String result = sb.toString();
        return Arrays.asList(result, isPalindrome(result));
    }

    public boolean isPalindrome(String s) {
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
}
```

This solution has a time complexity of O(n) where n is the length of the string s. The space complexity is also O(n) for storing the characters in the set. The isPalindrome function has a time complexity of O(n/2) which is O(n) in the worst case. So the overall time complexity is O(n). The space complexity is O(1) for the left and right pointers. So the overall space complexity is also O(n).