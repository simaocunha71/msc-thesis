        List<Integer> interspersedNumbers = new ArrayList<>();
        for (int i = 0; i < numbers.size(); i++) {
            interspersedNumbers.add(numbers.get(i));
            if (i != numbers.size() - 1) {
                interspersedNumbers.add(delimiter);
            }
        }
        return interspersedNumbers;
    }

public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.intersperse(Arrays.asList(1, 2, 3), 4)); //[1, 4, 2, 4, 3]
    }
}

This solution uses a for loop to iterate through the given list. It adds each number to a new list and if it is not the last number in the list, it also adds the delimiter. 
This solution has a time complexity of O(n) as it goes through the list once.

This problem could be solved by using Java 8's Stream API as well:

```java
    public List<Integer> intersperse(List<Integer> numbers, int delimiter) {
        return numbers.stream()
                .flatMap(i -> Stream.of(i, delimiter))
                .collect(Collectors.toList());
    }
```

This solution uses the Stream API to achieve the same result. It maps each number in the list to a Stream of the number and delimiter, then collects the results into a list.

The Stream API solution has the same time complexity as the for loop solution.
*/

// 