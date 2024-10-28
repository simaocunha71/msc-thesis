```java
import java.util.*;
import java.lang.*;

class Solution {
    public String intersection(List<Integer> interval1, List<Integer> interval2) {
        List<Integer> intersection = new ArrayList<>();
        for (int i = 0; i < interval1.size(); i++) {
            for (int j = 0; j < interval2.size(); j++) {
                if (interval1.get(i) >= interval2.get(j) && interval1.get(i) <= interval2.get(j + 1)) {
                    intersection.add(interval1.get(i));
                }
                if (interval2.get(j) >= interval1.get(i) && interval2.get(j) <= interval1.get(i + 1)) {
                    intersection.add(interval2.get(j));
                }
            }
        }
        Collections.sort(intersection);
        if (intersection.size() < 2) {
            return "NO";
        }
        int length = intersection.get(intersection.size() - 1) - intersection.get(0) + 1;
        return isPrime(length) ? "YES" : "NO";
    }

    private boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
```