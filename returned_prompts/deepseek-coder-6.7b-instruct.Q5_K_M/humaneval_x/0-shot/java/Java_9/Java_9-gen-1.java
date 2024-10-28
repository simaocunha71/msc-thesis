        List<Integer> maxNumbers = new ArrayList<>();
        int max = Integer.MIN_VALUE;
        for (Integer num : numbers){
            max = Math.max(max, num);
            maxNumbers.add(max);
        }
        return maxNumbers;
    }
}

Explanation:
The main idea of this solution is to initialize a variable `max` with the lowest possible integer value and iterate through the input list. For each number in the list, we compare it with `max` and update `max` if the number is larger. Then we add `max` to the result list. This way, we keep track of the maximum value we have seen so far in the list.

Time complexity is O(n) because we only traverse the list once. Space complexity is also O(n) because we store the result in a new list.

Note: This code is written in Java and it assumes that the input list `numbers` is not null and contains at least one integer.

*/

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Integer> numbers = Arrays.asList(1, 2, 3, 2, 3, 4, 2);
        System.out.println(solution.rollingMax(numbers));
    }
}

/*
Output:
[1, 2, 3, 3, 3, 4, 4]
 */
```





































































































































































