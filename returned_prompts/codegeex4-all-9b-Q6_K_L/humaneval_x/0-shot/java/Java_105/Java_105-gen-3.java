```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> byLength(List<Integer> arr) {
        List<Integer> arr1 = new ArrayList<>();
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) >= 1 && arr.get(i) <= 9) {
                arr1.add(arr.get(i));
            }
        }
        Collections.sort(arr1);
        Collections.reverse(arr1);
        List<String> arr2 = new ArrayList<>();
        for (int i = 0; i < arr1.size(); i++) {
            if (arr1.get(i) == 1) {
                arr2.add("One");
            }
            if (arr1.get(i) == 2) {
                arr2.add("Two");
            }
            if (arr1.get(i) == 3) {
                arr2.add("Three");
            }
            if (arr1.get(i) == 4) {
                arr2.add("Four");
            }
            if (arr1.get(i) == 5) {
                arr2.add("Five");
            }
            if (arr1.get(i) == 6) {
                arr2.add("Six");
            }
            if (arr1.get(i) == 7) {
                arr2.add("Seven");
            }
            if (arr1.get(i) == 8) {
                arr2.add("Eight");
            }
            if (arr1.get(i) == 9) {
                arr2.add("Nine");
            }
        }
        return arr2;
    }
}
```