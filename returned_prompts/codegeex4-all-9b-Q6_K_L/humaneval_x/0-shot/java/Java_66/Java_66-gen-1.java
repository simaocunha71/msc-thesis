Here is the Java solution for the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int digitSum(String s) {
        int sum = 0;
        for(char c : s.toCharArray()) {
            if(Character.isUpperCase(c)) {
                sum += (int) c;
            }
        }
        return sum;
    }
    
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.digitSum("abAB"));  // 131
        System.out.println(sol.digitSum("abcCd"));  // 67
        System.out.println(sol.digitSum("helloE"));  // 69
        System.out.println(sol.digitSum("woArBld"));  // 131
        System.out.println(sol.digitSum("aAaaaXa"));  // 153
    }
}
```
In this solution, we iterate over each character in the string. If the character is an uppercase letter, we add its ASCII value to the sum. The `Character.isUpperCase(char c)` method is used to check if the character is uppercase. The `(int) c` expression is used to get the ASCII value of the character.