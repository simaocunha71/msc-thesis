Here is a solution in Java:

```java
import java.util.*;

class Solution {
    public int smallestChange(List<Integer> arr) {
        int n = arr.size();
        int res = n;
        String s = "";
        for (int i : arr) {
            s += i + "";
        }
        for (int i = 0; i < n; i++) {
            s = s.substring(0, i) + s.substring(i + 1);
            int count = 0;
            for (int j = 0; j < n / 2; j++) {
                if (s.charAt(j) != s.charAt(n - j - 1)) {
                    count++;
                }
            }
            res = Math.min(res, count);
        }
        return res;
    }
}
```

This solution first converts the array to a string. Then it iterates over the string and for each character, it removes that character and calculates the number of characters that need to be changed to make the string a palindrome. The minimum number of changes is the result.

The time complexity of this solution is O(n^2) where n is the size of the array, because for each character, it needs to iterate over the rest of the string. The space complexity is O(n) for storing the string.