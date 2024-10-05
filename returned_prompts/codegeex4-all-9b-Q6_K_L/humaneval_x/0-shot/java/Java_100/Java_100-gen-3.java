```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> makeAPile(int n) {
        List<Integer> pile = new ArrayList<>();
        int currentLevel = n;
        for (int i = 0; i < n; i++) {
            pile.add(currentLevel);
            if (currentLevel % 2 == 0) {
                currentLevel += 2;
            } else {
                currentLevel += 2;
            }
        }
        return pile;
    }
}
```