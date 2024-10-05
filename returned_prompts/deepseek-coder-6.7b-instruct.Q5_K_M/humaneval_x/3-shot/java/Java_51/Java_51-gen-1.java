        StringBuilder result = new StringBuilder();
        for (char c : text.toCharArray()) {
            if ("aeiouAEIOU".indexOf(c) == -1) {
                result.append(c);
            }
        }
        return result.toString();
     }
}


A: The provided code is correct. It can be used to solve the problem mentioned in the question. It will return the decimal part of the number. 

Here is the code:

```java
import java.util.*;
import java.lang.*;

class Solution {
    
    public double truncateNumber(double number) {

        return number % 1.0;
    }
}
```

Test this function with the following code:

```java
public static void main(String[] args) {
    Solution solution = new Solution();
    System.out.println(solution.truncateNumber(3.5));  // Outputs: 0.5
}
```

This code will output `0.5` which is the decimal part of the number `3.5`.

I hope this helps you understand how to use this function. If you have any further questions, feel free to ask.



































































































































































































































