        List<Integer> result = new ArrayList<Integer>();
        for (Integer num : x) {
            if (hasUniqueDigits(num)) {
                result.add(num);
            }
        }
        Collections.sort(result);
        return result;
    }

    private boolean hasUniqueDigits(Integer num) {
        Set<Integer> digits = new HashSet<Integer>();
        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                return false;
            }
            if (!digits.add(digit)) {
                return false;
            }
            num /= 10;
        }
        return true;
    }
}

```

## Answer 2:
```java
import java.util.*;
import java.lang.*;

class Solution  {
    public List<Integer> uniqueDigits(List<Integer> x) {
        List<Integer> result = new ArrayList<>();
        for (Integer num : x) {
            if (hasUniqueDigits(num)) {
                result.add(num);
            }
        }
        Collections.sort(result);
        return result;
    }

    private boolean hasUniqueDigits(Integer num) {
        Set<Integer> digits = new HashSet<>();
        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                return false;
            }
            if (!digits.add(digit)) {
                return false;
            }
            num /= 10;
        }
        return true;
    }
}

```

## Answer 3:
```java
import java.util.*;
import java.lang.*;

class Solution  {
    public List<Integer> uniqueDigits(List<Integer> x) {
        List<Integer> result = new ArrayList<>();
        for (Integer num : x) {
            if (hasUniqueDigits(num)) {
                result.add(num);
            }
        }
       