        StringBuilder result = new StringBuilder();
        for(int i = 0; i < a.length(); i++){
            if(a.charAt(i) == b.charAt(i)){
                result.append('0');
            }
            else{
                result.append('1');
            }
        }
        return result.toString();
    }
}


A: It seems like you've copied the code directly, but there is a small issue. The input parameters for your method are not the same as the question states. 
Here's the corrected version:

```java
import java.util.*;
import java.lang.*;

class Solution  {
    /**
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> stringXor("010", "110")
    "100"
      */
    public String stringXor(String a, String b)  {
        StringBuilder result = new StringBuilder();
        for(int i = 0; i < a.length(); i++){
            if(a.charAt(i) == b.charAt(i)){
                result.append('0');
            }
            else{
                result.append('1');
            }
        }
        return result.toString();
    }
}
```

This code will work as expected. It loops through each character of the input strings and checks if they are the same. If they are the same, it appends a '0' to the result string. If they are different, it appends a '1'.
This will give you the XOR result of the two binary strings.

Please note that this code assumes that the input strings are of the same length.