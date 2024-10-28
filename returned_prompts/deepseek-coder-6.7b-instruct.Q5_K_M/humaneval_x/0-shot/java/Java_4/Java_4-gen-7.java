        double sum = 0;
        double mean = 0;
        double mad = 0;

        for (double num : numbers) {
            sum += num;
        }

        mean = sum / numbers.size();

        for (double num : numbers) {
            mad += Math.abs(num - mean);
        }

        return mad / numbers.size();
    }
}

Explanation:
The Mean Absolute Deviation (MAD) is the average of the absolute differences from the Mean.

We first calculate the mean by summing all numbers and dividing by the count of numbers.

Then we calculate the absolute difference from the mean for each number and sum these up.

Finally, we divide the sum of these absolute differences by the count of numbers to get the MAD.

The time complexity of this solution is O(n), where n is the number of elements in the list. This is because we are performing a single pass over the list to calculate the sum of the numbers, another pass to calculate the mean, and another pass to calculate the MAD.

The space complexity is O(1) as we are using a constant amount of space to store the sum, mean, and MAD.
*/

// Test Cases

// 1. Test with 4 numbers
Solution s = new Solution();
List<Double> numbers = Arrays.asList(1.0, 2.0, 3.0, 4.0);
System.out.println(s.meanAbsoluteDeviation(numbers)); // Expected: 1.0

// 2. Test with negative numbers
numbers = Arrays.asList(-1.0, -2.0, -3.0, -4.0);
System.out.println(s.meanAbsoluteDeviation(numbers)); // Expected: 1.0

// 3. Test with a mix of positive and negative numbers
numbers = Arrays.asList(-1.0, 2.0, -3.0, 4.0);
System.out.println(s.meanAbsoluteDeviation(numbers)); // Expected: 2.0

// 4. Test with a single number
numbers = Ar