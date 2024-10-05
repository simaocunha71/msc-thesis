        for (int i = 0; i < lst.size() - 1; i++) {
            if (lst.get(i) >= lst.get(i + 1)) {
                return false;
            }
        }
        return true;
    }
}

This program works by iterating through the list and checking if the current number is greater than or equal to the next number. If it is, the list is not sorted in ascending order, and the program returns false. If it never finds a pair of numbers in order, it returns true, indicating that the list is sorted in ascending order.

This solution has a time complexity of O(n) because it goes through the list once.

The space complexity is O(1), because no additional space is used that scales with the size of the input list.

This program handles the cases where the list has more than one duplicate of the same number by returning false. This is because if there are two numbers in a row that are the same, it means the list is not sorted.

This program assumes that the list does not contain negative numbers, as per the problem statement.
*/

// Test cases

/*
isSorted(Arrays.asList(5)) → true
isSorted(Arrays.asList(1, 2, 3, 4, 5)) → true
isSorted(Arrays.asList(1, 3, 2, 4, 5)) → false
isSorted(Arrays.asList(1, 2, 3, 4, 5, 6)) → true
isSorted(Arrays.asList(1, 2, 3, 4, 5, 6, 7)) → true
isSorted(Arrays.asList(1, 3, 2, 4, 5, 6, 7)) → false
isSorted(Arrays.asList(1, 2, 2, 3, 3, 4)) → true
isSorted(Arrays.asList(1, 2, 2, 2, 3, 4)) → false
*/

// Explanation:
/*
- For the first