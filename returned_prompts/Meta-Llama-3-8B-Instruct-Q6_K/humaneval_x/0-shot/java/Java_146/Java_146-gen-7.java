    public int specialFilter(List<Integer> nums) {
        int count = 0;
        for (int num : nums) {
            if (Math.abs(num) > 10 && isOdd(num)) {
                count++;
            }
        }
        return count;
    }

    public boolean isOdd(int num) {
        int lastDigit = num % 10;
        int firstDigit = num / 100;
        if (firstDigit == 0) {
            firstDigit = num / 10 % 10;
        }
        return lastDigit % 2 != 0 && firstDigit % 2 != 0;
    }
}  // The function specialFilter takes a list of integers as input. It iterates through each number in the list. If the absolute value of the number is greater than 10 and the function isOdd returns true for the number, it increments a count variable. The function isOdd checks if the last digit and the first digit of a number are odd. It returns true if both conditions are met, and false otherwise. The function specialFilter returns the count variable at the end, which represents the number of elements in the array that are greater than 10 and both first and last digits of a number are odd.  // The function isOdd checks if the last digit and the first digit of a number are odd. It returns true if both conditions are met, and false otherwise. It handles the case where the first digit is 0, as in the case of two-digit numbers.  // The function specialFilter uses the isOdd function to filter the input list and count the numbers that meet the specified conditions. It returns the count at the end.  // The function specialFilter is designed to handle negative numbers by taking the absolute value of the input number. This ensures that the function works correctly for negative numbers.  // The function specialFilter has a time complexity of O(n), where n is the number of elements in the input list. This is because it iterates through each element in the list once. The space complexity is O(1), as it only uses a constant amount of space to store the count variable and the input list.  // The function isOdd has a time complexity of O(1), as it only performs a constant number of operations to check the digits of a number. The space complexity is O(1), as it only uses a constant amount of space to store the last digit and the first digit of a number.  // The function special