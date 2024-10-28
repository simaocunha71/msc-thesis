```java
import java.util.*;

class Solution {
    public List<Integer> orderByPoints(List<Integer> nums) {
        // Convert list to list of pairs (num, sum of digits)
        List<Map.Entry<Integer, Integer>> list = new ArrayList<>();
        for (int num : nums) {
            int sumOfDigits = getSumOfDigits(num);
            list.add(new AbstractMap.SimpleEntry<>(num, sumOfDigits));
        }

        // Sort the list of pairs
        Collections.sort(list, new Comparator<Map.Entry<Integer, Integer>>() {
            @Override
            public int compare(Map.Entry<Integer, Integer> o1, Map.Entry<Integer, Integer> o2) {
                if (o1.getValue().equals(o2.getValue())) {
                    return Integer.compare(o1.getKey().hashCode(), o2.getKey().hashCode());
                } else {
                    return Integer.compare(o1.getValue(), o2.getValue());
                }
            }
        });

        // Convert back to list of integers
        List<Integer> result = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : list) {
            result.add(entry.getKey());
        }

        return result;
    }

    private int getSumOfDigits(int num) {
        int sum = 0;
        while (num != 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}
```


Explanation:

1. First, we create a new list where each element is a pair containing the original number and the sum of its digits.
2. We then sort this list of pairs based on the sum of digits. If two numbers have the same sum of digits, we use the original index of the number in the list as the secondary sorting criterion.
3. Finally, we convert the sorted list of pairs back to a list of integers.

The `getSumOfDigits` method is used to calculate the sum of digits of a given number. It does this by repeatedly dividing the number by 10 and adding the remainder to the sum, until the number becomes 0.