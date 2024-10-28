```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> byLength(List<Integer> arr) {
        String[] words = {"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) > 0 && arr.get(i) < 10) {
                result.add(arr.get(i));
            }
        }
        Collections.sort(result);
        Collections.reverse(result);
        List<String> resultWords = new ArrayList<>();
        for (int i = 0; i < result.size(); i++) {
            resultWords.add(words[result.get(i) - 1]);
        }
        return resultWords;
    }
}
```