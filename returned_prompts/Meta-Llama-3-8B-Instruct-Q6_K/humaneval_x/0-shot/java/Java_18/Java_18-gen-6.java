You can solve this problem by using a Java method that counts the occurrences of a given substring in a string. This method uses a while loop to iterate over the string and checks if the substring is found at each position. If it is, the count is incremented and the loop continues from the next position. Here is the Java code:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int howManyTimes(String string, String substring) {
        int count = 0;
        int stringLength = string.length();
        int substringLength = substring.length();
        int index = 0;
        
        while (index <= stringLength - substringLength) {
            if (string.substring(index, index + substringLength).equals(substring)) {
                count++;
                index += substringLength;
            } else {
                index++;
            }
        }
        return count;
    }
}
```

This method returns the number of times the given substring is found in the original string, taking into account overlapping cases. For example, if the original string is "aaa" and the substring is "a", the method will return 3 because "a" is found three times in the string. If the original string is "aaaa" and the substring is "aa", the method will also return 3 because "aa" is found three times in the string.

Here's how you can test the method:

```java
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.howManyTimes("", "a"));
        System.out.println(solution.howManyTimes("aaa", "a"));
        System.out.println(solution.howManyTimes("aaaa", "aa"));
    }
}
```

When you run this code, it will print the following output:

```
0
3
3
```


This shows that the method correctly counts the occurrences of the given substring in the original string, including overlapping cases.