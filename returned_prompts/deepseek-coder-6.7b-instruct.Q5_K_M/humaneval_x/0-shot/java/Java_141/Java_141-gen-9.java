        // your code goes here

    }
}


A: Here is your solution:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public String filenameCheck(String file_name) {
        // check if there is exactly one dot
        if (file_name.indexOf('.') == file_name.lastIndexOf('.')) {
            String[] splitResult = file_name.split("\\.");
            // check if the substring before the dot is not empty and starts with a letter
            if (!splitResult[0].isEmpty() && Character.isLetter(splitResult[0].charAt(0))) {
                // check if there are less than or equal to three digits in the substring before the dot
                if (splitResult[0].replaceAll("[^0-9]", "").length() <= 3) {
                    // check if the substring after the dot is one of these: ["txt", "exe", "dll"]
                    if (splitResult[1].equals("txt") || splitResult[1].equals("exe") || splitResult[1].equals("dll")) {
                        return "Yes";
                    }
                }
            }
        }
        return "No";
    }
}
```

This function works by splitting the file name into two parts: before and after the dot. Then it checks each condition. If any condition is not met, it immediately returns "No". If all conditions are met, it returns "Yes".

Note: This solution assumes that the file name does not contain any other special characters or spaces. If there is a possibility of containing those, you should add additional checks.

Also, please note that file names are case sensitive, so the substring before the dot should start with a capital letter not a lowercase letter. If you want to ignore the case, you can convert the file name to lower case before checking.

The function filenameCheck("example.txt") will return "Yes", and filenameCheck("1example.dll") will return "No".

```java
Solution solution = new Solution();
System.out.println(solution.filenameCheck("example.txt"));  // prints "Yes"
System.out.println(solution.filenameCheck("