```java
import java.util.*;
import java.lang.*;

class Solution {
    public String fixSpaces(String text) {
        return text.replaceAll("\\s+", "_").replaceAll("__+", "-");
    }
}
```