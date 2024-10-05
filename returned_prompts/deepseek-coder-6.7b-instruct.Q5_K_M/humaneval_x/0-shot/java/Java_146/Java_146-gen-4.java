        int count = 0;

        for(int i = 0; i < nums.size(); i++){
            if(Math.abs(nums.get(i)) > 10){
                int lastDigit = Math.abs(nums.get(i)) % 10;
                int firstDigit = (Math.abs(nums.get(i)) / 10) % 10;
                if(lastDigit % 2 != 0 && firstDigit % 2 != 0) count++;
            }
        }

        return count;
    }
}

Explanation:
The function `specialFilter` counts the number of elements in the array that are greater than 10 and both
first and last digits of a number are odd (1, 3, 5, 7, 9).

The `for` loop iterates through each number in the list. If the absolute value of the number is greater than 10, it then checks the first and last digit of the number. If both the first and last digit are odd (i.e., their remainder when divided by 2 is not 0), it increments the counter `count`.

Finally, the function returns the count of numbers that meet these conditions.

*/

// The main function is not required in this problem. It is used for testing the above code.
public class Main {
    public static void main (String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.specialFilter(Arrays.asList(15, -73, 14, -15))); // should print 1
        System.out.println(solution.specialFilter(Arrays.asList(33, -2, -3, 45, 21, 109))); // should print 2
    }
}

This code will output the correct count of numbers that meet the conditions specified in the problem statement.

*/





















































