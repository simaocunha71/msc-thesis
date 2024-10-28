int specialFilter(vector<int> nums) {
    int count = 0;
    int n = nums.size();
    for (int i = 0; i < n; i++) {
        if (nums[i] > 10) {
            int temp = nums[i];
            int first = temp / 10;
            int last = temp % 10;
            if ((first % 2 != 0) && (last % 2 != 0)) {
                count++;
            }
        }
    }
    return count;
}

Explanation:
The function specialFilter takes a vector of numbers as an input and returns the number of elements in the vector that satisfy two conditions:
1. The element is greater than 10.
2. The first and last digits of the number are both odd (1, 3, 5, 7, 9).

The function loops through all the elements in the vector and checks if the number is greater than 10. If so, it separates the first and last digits of the number by dividing and modulo operations. It then checks if both digits are odd. If they are, it increments the count variable.

Finally, the function returns the count of numbers that satisfy the conditions.

The provided example in the main function demonstrates how to use the specialFilter function with a sample vector of numbers.







