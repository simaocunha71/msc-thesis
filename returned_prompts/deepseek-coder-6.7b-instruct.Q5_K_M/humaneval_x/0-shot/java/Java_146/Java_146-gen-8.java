        int count = 0;
        for (int num : nums) {
            if (Math.abs(num) > 10 && isFirstAndLastOdd(num)) {
                count++;
            }
        }
        return count;
    }

    private boolean isFirstAndLastOdd(int num) {
        int lastDigit = Math.abs(num % 10);
        int firstDigit = 0;
        while (num != 0) {
            firstDigit = Math.abs(num % 10);
            num /= 10;
        }
        return lastDigit % 2 != 0 && firstDigit % 2 != 0;
    }
}

Note: The function specialFilter checks the absolute value of each number in the list (using Math.abs) to ensure it's greater than 10, even if the number is negative. The function isFirstAndLastOdd takes an integer and checks if the last digit and first digit are odd. It does this by taking the modulo 10 of the number to get the last digit, and by repeatedly dividing the number by 10 until it's 0 to get the first digit. It then checks if these digits are odd by taking the modulo 2 of them. If they're both 1 (which is what odd numbers have), the function returns true, otherwise it returns false.

















*/

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.specialFilter(Arrays.asList(15, -73, 14, -15)));  // Outputs: 1
        System.out.println(sol.specialFilter(Arrays.asList(33, -2, -3, 45, 21, 109)));  // Outputs: 2
    }
}



















































