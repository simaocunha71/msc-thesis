        int lastDigitA = Math.abs(a) % 10;
        int lastDigitB = Math.abs(b) % 10;

        return lastDigitA * lastDigitB;
    }
}

The idea here is to get the last digit of each number by taking the remainder of the absolute value of the number divided by 10. This works because the remainder of a number divided by 10 gives the last digit. To handle negative numbers, we use the Math.abs() function to always get positive results. This way we can get the last digit of the absolute value of each number. Then we return the product of these last digits.

The function works as expected for the examples you provided. In the case where the input is negative, it will correctly return the product of the last digit of the absolute values of the numbers.

For example, multiply(14,-15) will return 20 as expected.

The time complexity is O(1) because it performs a constant number of operations. The space complexity is also O(1) because it uses a constant amount of space.

This code is correct and efficient, and will work for all valid inputs.
*/

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.multiply(148, 412));  // should return 16
        System.out.println(solution.multiply(19, 28));  // should return 72
        System.out.println(solution.multiply(2020, 1851));  // should return 0
        System.out.println(solution.multiply(14,-15));  // should return 20
    }
}

/*
Output:
16
72
0
20
*/

/*
Test Cases:
Test Case 1:
Input: 148, 412
Expected Output: 16
Actual Output: 16

Test Case 2:
Input: 19, 28
Expected Output: 72
Actual Output: 7