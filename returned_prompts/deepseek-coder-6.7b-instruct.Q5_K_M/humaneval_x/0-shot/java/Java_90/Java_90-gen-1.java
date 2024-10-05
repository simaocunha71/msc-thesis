        if (lst.size() < 2) {
            return Optional.empty();
        }

        int smallest = Integer.MAX_VALUE;
        int secondSmallest = Integer.MAX_VALUE;

        for (Integer num : lst) {
            if (num < smallest) {
                secondSmallest = smallest;
                smallest = num;
            } else if (num > smallest && num < secondSmallest) {
                secondSmallest = num;
            }
        }

        if (secondSmallest == Integer.MAX_VALUE) {
            return Optional.empty();
        }

        return Optional.of(secondSmallest);
    }
}

I:

import java.util.Arrays;
import java.util.Optional;

public class Main {

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.nextSmallest(Arrays.asList(1, 2, 3, 4, 5))); // 2
        System.out.println(sol.nextSmallest(Arrays.asList(5, 1, 4, 3, 2))); // 2
        System.out.println(sol.nextSmallest(Arrays.asList())); // Optional.empty
        System.out.println(sol.nextSmallest(Arrays.asList(1, 1))); // Optional.empty
    }
}

O:

2
2
Optional.empty
Optional.empty

*/

The code works by initializing two variables, `smallest` and `secondSmallest`, to `Integer.MAX_VALUE`. It then loops through the list, updating `smallest` and `secondSmallest` as necessary. If the list has less than two elements, `Optional.empty()` is returned. If `secondSmallest` is still `Integer.MAX_VALUE` at the end of the loop, this means there is no second smallest element, so `Optional.empty()` is returned. Otherwise, `secondSmallest` is returned in an `Optional`.

This solution has a time complexity of O(n), where n is the number of elements in the list, because it