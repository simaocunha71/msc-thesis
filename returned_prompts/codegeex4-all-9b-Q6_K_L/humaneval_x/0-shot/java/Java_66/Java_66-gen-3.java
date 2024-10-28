```java
import java.util.*;
import java.lang.*;

class Solution {
    public int digitSum(String s) {
        int sum = 0;
        for (char c : s.toCharArray()) {
            if (Character.isUpperCase(c)) {
                sum += (int) c;
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.digitSum("")); // 0
        System.out.println(solution.digitSum("abAB")); // 131
        System.out.println(solution.digitSum("abcCd")); // 67
        System.out.println(solution.digitSum("helloE")); // 69
        System.out.println(solution.digitSum("woArBld")); // 131
        System.out.println(solution.digitSum("aAaaaXa")); // 153
    }
}
```