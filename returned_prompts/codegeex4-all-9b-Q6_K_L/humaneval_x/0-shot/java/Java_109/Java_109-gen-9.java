```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean moveOneBall(List<Integer> arr) {
        if(arr.size() == 0) return true;
        
        int minIndex = 0;
        for(int i = 1; i < arr.size(); i++) {
            if(arr.get(i) < arr.get(minIndex)) {
                minIndex = i;
            }
        }
        
        List<Integer> temp = new ArrayList<>(arr);
        for(int i = 0; i < minIndex; i++) {
            temp.add(temp.remove(0));
        }
        
        for(int i = 0; i < temp.size()-1; i++) {
            if(temp.get(i) > temp.get(i+1)) return false;
        }
        
        return true;
    }
}
```