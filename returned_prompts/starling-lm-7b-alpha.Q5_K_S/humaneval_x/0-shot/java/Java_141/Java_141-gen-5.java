        String ans = "Yes";
        int count = 0;
        for (int i = 0; i < file_name.length(); i++) {
            if (file_name.charAt(i) >= '0' && file_name.charAt(i) <= '9') {
                count++;
            }
            if (file_name.charAt(i) == '.') {
                if (count > 3) {
                    ans = "No";
                    break;
                }
                count = 0;
            }
        }
        if (count > 3) {
            ans = "No";
        }
        if (file_name.charAt(0) < 'a' || file_name.charAt(0) > 'z'
                && file_name.charAt(0) < 'A' || file_name.charAt(0) > 'Z') {
            ans = "No";
        }
        if (!file_name.contains(".")) {
            ans = "No";
        }
        if (!file_name.substring(file_name.length() - 3).equals("txt") && !file_name.substring(file_name.length() - 3).equals("exe") && !file_name.substring(file_name.length() - 3).equals("dll")) {
            ans = "No";
        }
        return ans;
    }
}








```

Answer:

Here's a function that checks if a given file name is valid according to the rules you provided:

```java
import java.util.*;

public class FileNameCheck {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.filenameCheck("example.txt"));  // "Yes"
        System.out.println(solution.filenameCheck("1example.dll")); // "No"
    }
}

class Solution {
    public String filenameCheck(String file_name) {
        String ans = "Yes";
        int count = 0;
        for (int i