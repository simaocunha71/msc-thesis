        int count = 0;
        for (int num : nums) {
            if (num > 10 && isOdd(num) && isOddDigit(num)) {
                count += 1;
            }
        }
        return count;
    }

    private boolean isOdd(int num) {
        return num % 2 != 0;
    }

    private boolean isOddDigit(int num) {
        int first_digit = Math.abs(num) / 10;
        int last_digit = Math.abs(num) % 10;
        return isOdd(first_digit) && isOdd(last_digit);
    }
}

