        // Create a new list to store the sorted results
        List<Integer> sortedList = new ArrayList<>(nums);

        // Create a new comparator to sort the list based on the sum of digits
        Comparator<Integer> comparator = new Comparator<Integer>() {
            @Override
            public int compare(Integer num1, Integer num2) {
                // Calculate the sum of digits for num1 and num2
                int sum1 = getDigitSum(Math.abs(num1));
                int sum2 = getDigitSum(Math.abs(num2));

                // If the sum of digits are equal, compare their indices
                if (sum1 == sum2) {
                    return nums.indexOf(num1) - nums.indexOf(num2);
                }

                // Otherwise, compare the sums of digits
                return sum1 - sum2;
            }
        };

        // Sort the list using the comparator
        Collections.sort(sortedList, comparator);

        return sortedList;
    }

    // Helper function to calculate the sum of digits for a given number
    private int getDigitSum(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}

This code first creates a new list to store the sorted results. It then creates a new comparator that compares the sum of digits of two numbers. If the sum of digits are equal, it compares their indices in the original list. The list is then sorted using this comparator. The helper function `getDigitSum` is used to calculate the sum of digits for a given number.

This code works by creating a new list to store the sorted results, and then creating a new comparator to sort the list based on the sum of digits. The comparator first compares the sum of digits of two numbers. If the sums are equal, it compares the indices of the numbers in the original list. The list is then sorted using this comparator. The helper function `getDigitSum` is used to calculate the sum of digits for