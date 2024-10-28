```java
import java.util.*;
import java.lang.*;

class Solution {
    public String fixSpaces(String text) {
        return text.trim().replaceAll(" +", "_").replaceAll("__+", "-");
    }
}
```
The `trim()` method removes leading and trailing spaces.
The `replaceAll(" +", "_")` method replaces one or more consecutive spaces with an underscore.
The `replaceAll("__+", "-")` method replaces two or more consecutive underscores with a dash.