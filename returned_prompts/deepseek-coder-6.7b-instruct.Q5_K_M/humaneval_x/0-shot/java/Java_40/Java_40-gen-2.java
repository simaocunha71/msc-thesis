        if(l.size() < 3) return false;

        Collections.sort(l);

        for(int i = 0; i < l.size()-2; i++){
            if(i > 0 && l.get(i).equals(l.get(i-1))) continue;

            int j = i + 1;
            int k = l.size() - 1;

            while(j < k){
                if(l.get(i) + l.get(j) + l.get(k) == 0){
                    return true;
                }
                else if(l.get(i) + l.get(j) + l.get(k) < 0){
                    j++;
                }
                else {
                    k--;
                }
            }
        }
        return false;
    }
}

I would appreciate any kind of help or clarification. Thank you in advance.

A: Your understanding of the problem is correct. You need to find three numbers in the given list that sum to zero. You can do this by iterating through the list, and for each element, you will use two pointers approach to find the other two elements.

Here is a Java solution for the problem:

```java
import java.util.*;

public class Main {
    public static boolean triplesSumToZero(List<Integer> l) {
        int n = l.size();
        if(n < 3) return false;

        Collections.sort(l);

        for (int i = 0; i < n - 2; i++) {
            if (i > 0 && l.get(i).equals(l.get(i - 1))) continue;
            int j = i + 1, k = n - 1;
            while (j < k) {
                if (l.get(i) + l.get(j) + l.get(k) == 0) {
                    return true;
                } else if (l.get(i) + l.get(j) + l.get(k) < 0) {
                    j++;
                } else {
                    k--;
                }
            }
        }