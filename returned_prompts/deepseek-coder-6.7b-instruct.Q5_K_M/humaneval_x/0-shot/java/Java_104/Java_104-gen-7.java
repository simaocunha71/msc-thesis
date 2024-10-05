        List<Integer> result = new ArrayList<>();

        for (Integer num : x) {
            if (hasUniqueDigits(num)) {
                result.add(num);
            }
        }

        Collections.sort(result);
        return result;
    }

    private boolean hasUniqueDigits(Integer num) {
        Set<Integer> digits = new HashSet<>();

        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                return false;
            }
            if (!digits.add(digit)) {
                return false;
            }
            num /= 10;
        }

        return true;
    }

}

The class Solution has a method uniqueDigits that takes a List of Integers as parameter. It filters the list and adds to the result list only the numbers that have unique digits and no even digit. The result list is then sorted and returned. The helper method hasUniqueDigits checks if a number has unique digits and no even digit. It returns true if the number meets these conditions and false otherwise.

In the main method, we create a new instance of the Solution class and call the uniqueDigits method with a list of integers as the argument. The resulting list of integers is printed to the console.

The time complexity of this solution is O(n*m), where n is the number of elements in the input list and m is the average number of digits in the numbers in the input list. This is because we are iterating over each number in the list and for each number, we are iterating over each digit in the number. The space complexity is O(n), as we are storing the result in a separate list.

In the uniqueDigits method, we first initialize an empty list to store the result. We then iterate over each number in the input list. For each number, we check if it has unique digits and no even digit by calling the hasUniqueDigits method. If it does, we add it to the result list. Finally, we sort the result list and return it.

In the hasUniqueDigits method, we initialize an empty set to store the digits. We then iterate