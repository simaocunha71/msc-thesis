        int count = 0;
        for (int num : nums) {
            if (num > 10) {
                int lastDigit = Math.abs(num % 10);
                int firstDigit = Math.abs(num / 10);
                if (lastDigit % 2 == 1 && firstDigit % 2 == 1) {
                    count++;
                }
            }
        }
        return count;
    }
}


A: Here is the corrected code.

public class Solution {

    public static void main(String[] args) {
        List<Integer> nums = Arrays.asList(15, -73, 14, -15);
        System.out.println(specialFilter(nums));
        nums = Arrays.asList(33, -2, -3, 45, 21, 109);
        System.out.println(specialFilter(nums));
    }

    public static int specialFilter(List<Integer> nums) {
        int count = 0;
        for (int num : nums) {
            if (num > 10) {
                int lastDigit = Math.abs(num % 10);
                int firstDigit = Math.abs(num / 10);
                if (lastDigit % 2 == 1 && firstDigit % 2 == 1) {
                    count++;
                }
            }
        }
        return count;
    }
}


This code takes an array of numbers as input, iterates over them, checks each number to see if it is greater than 10 and if its first and last digits are both odd. If it does, it increments a counter. The function then returns the count.

A: Your code is almost correct. Just make sure you're using the correct modulo operation to get the last digit.

public int specialFilter(List<Integer> nums) {
    int count = 0;
    for (int num : nums) {
        if (num > 10) {
            int lastDigit = Math.abs(num % 10);
            int firstDig