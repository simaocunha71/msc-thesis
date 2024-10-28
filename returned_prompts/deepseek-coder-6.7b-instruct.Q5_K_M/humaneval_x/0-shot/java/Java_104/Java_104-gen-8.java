        List<Integer> result = new ArrayList<>();
        for (Integer num : x) {
            if (!hasEvenDigit(num)) {
                result.add(num);
            }
        }
        Collections.sort(result);
        return result;
    }

    private boolean hasEvenDigit(Integer num) {
        while (num > 0) {
            if ((num % 10) % 2 == 0) {
                return true;
            }
            num /= 10;
        }
        return false;
    }
}

Explanation:
This solution creates a new list of integers which contains no even digits in them. It uses a helper function 'hasEvenDigit' to check if an integer contains an even digit. If it doesn't, it adds the integer to the result list. Finally, it sorts the result list in ascending order and returns it.

In the 'uniqueDigits' function, the time complexity is O(n*m) where n is the size of the input list and m is the average number of digits in the numbers in the list. The space complexity is O(n) as we are storing the result in a new list.

The 'hasEvenDigit' function has a time complexity of O(m) as it has to check each digit in the number. The space complexity is O(1) as it doesn't use any extra space.

The overall time complexity of the solution is O(n*m) and the space complexity is O(n).

This solution assumes that the input list x consists of positive integers.

Also note that this solution does not handle cases where the input list contains non-integer values.

To handle such cases, you can add a check at the start of the 'uniqueDigits' function to ensure that all elements in the list are integers. If they are not, you can throw an exception or return an error message.

This solution also assumes that the input list does not contain duplicate numbers. If it does, you would need to add a check to remove duplicates before adding them to the result list.

If you want to keep duplicates in the result list, you can remove the check that removes duplicates from the 'uniqueDigits' function.
  
  This solution uses Java language