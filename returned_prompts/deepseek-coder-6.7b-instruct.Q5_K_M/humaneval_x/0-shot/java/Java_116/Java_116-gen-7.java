        Collections.sort(arr, new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                int bitCount1 = Integer.bitCount(o1);
                int bitCount2 = Integer.bitCount(o2);

                if (bitCount1 == bitCount2) {
                    return o1.compareTo(o2);
                } else {
                    return bitCount1 - bitCount2;
                }
            }
        });
        return arr;
    }
}


A: Here is the solution of the problem using Java 8 Streams.

```
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Solution {
    public List<Integer> sortArray(List<Integer> arr) {
        return arr.stream()
                .sorted((a, b) -> {
                    int bitCountA = Integer.bitCount(a);
                    int bitCountB = Integer.bitCount(b);

                    if (bitCountA == bitCountB) {
                        return a.compareTo(b);
                    } else {
                        return Integer.compare(bitCountA, bitCountB);
                    }
                })
                .collect(Collectors.toList());
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.sortArray(Arrays.asList(1, 5, 2, 3, 4)));
        System.out.println(solution.sortArray(Arrays.asList(-2, -3, -4, -5, -6)));
        System.out.println(solution.sortArray(Arrays.asList(1, 0, 2, 3, 4)));
    }
}
```

This code sorts the list of integers based on the number of ones in their binary representation, and then on the decimal value of the integers if the number of ones are the same.

It uses Java 8 Streams to create a new sorted list from the input list. The sorted method of the Stream accepts a Com