        List<Integer> maxList = new ArrayList<Integer>();
        int max = Integer.MIN_VALUE;

        for (int num : numbers) {
            max = Math.max(max, num);
            maxList.add(max);
        }

        return maxList;
    }
}

Explanation:

The problem is asking us to find the maximum number in the list up to the current position.

We initialize maxList as an empty list and max as the smallest integer.

We then run a for loop that goes through each number in the list.

In each iteration, we set max to the maximum of max and the current number. This will always be the maximum number up to this point.

We then add max to maxList.

Finally, we return maxList.

This solution has a time complexity of O(n), where n is the length of the list, and a space complexity of O(n), since we are storing the result in a new list.

This solution assumes that the list is not empty and that all elements are integers. If these assumptions are not true, we need to add error checking to the start of the function.

The Java 8 stream API could be used to make it more concise:

```java
public List<Integer> rollingMax(List<Integer> numbers) {
    return IntStream.range(0, numbers.size())
        .map(i -> Math.max(numbers.get(i), i > 0 ? maxList.get(i - 1) : Integer.MIN_VALUE))
        .boxed()
        .collect(Collectors.toList());
}
```
This version does the same thing as the previous one, but in a more stream-like style. It's a bit more complex and harder to understand though.

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
[1, 2, 3