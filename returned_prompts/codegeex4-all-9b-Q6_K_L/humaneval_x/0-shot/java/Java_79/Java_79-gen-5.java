```java
import java.util.*;
import java.lang.*;

class Solution {
    public String decimalToBinary(int decimal) {
        String binaryString = Integer.toBinaryString(decimal);
        return "db" + binaryString + "db";
    }
}
```
