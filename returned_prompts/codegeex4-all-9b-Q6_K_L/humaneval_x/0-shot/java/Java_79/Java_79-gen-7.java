Here is a simple way to solve this problem in Java. We can use the built-in Integer.toBinaryString method to convert the decimal number to binary. We add "db" at the beginning and at the end of the string to match the problem's requirements. Here is the complete code:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public String decimalToBinary(int decimal) {
        String binary = Integer.toBinaryString(decimal);
        return "db" + binary + "db";
    }
}
```

In this code, the decimalToBinary method takes an integer decimal as input and converts it to binary using the Integer.toBinaryString method. Then, it adds "db" at the beginning and at the end of the binary string and returns the result.