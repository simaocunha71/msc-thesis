        List<Integer> result = new ArrayList<>();
        int max = Integer.MIN_VALUE;

        for (int num : numbers) {
            if (num > max) {
                max = num;
            }
            result.add(max);
        }

        return result;
    }
}

Explanation:

This solution uses a for-each loop to iterate over each number in the input list. If the current number is greater than the current max, it is stored as the new max. The current max is then added to the result list. This continues until all numbers in the input list have been processed.

The result list will contain the rolling maximum at each index in the input list, as required by the problem.

The time complexity of this solution is O(n), as it makes a single pass over the input list. The space complexity is also O(n), as it creates a new list to store the results.

The rollingMax function works as expected for the given example and also handles edge cases such as an empty list.

It is important to note that this solution assumes that the input list will not be null. If the input list could be null, a null check should be included at the start of the function.

This solution is written in Java, but it can be easily translated to other programming languages.
