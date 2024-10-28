        return numbers.stream()
                .filter(i -> Collections.frequency(numbers, i) == 1)
                .collect(Collectors.toList());

This solution is correct, but it can be optimized by using a HashSet to keep track of the numbers that have already been seen. You can iterate through the numbers list and add each number to the HashSet. If a number is already in the HashSet, you skip it. Otherwise, you add the number to the result list. This solution is O(n), which is much faster than the