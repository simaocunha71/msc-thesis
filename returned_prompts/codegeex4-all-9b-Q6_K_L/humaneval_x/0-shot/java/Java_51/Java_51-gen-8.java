```java
import java.util.*;
import java.lang.*;

class Solution {
    public String removeVowels(String text) {
        return text.replaceAll("[aeiouAEIOU]", "");
    }
}
```