        int count = 0;
        for (int num : nums) {
            if (num > 10 && isFirstAndLastOddDigits(num)) {
                count++;
            }
        }
        return count;
    }

    private boolean isFirstAndLastOddDigits(int num) {
        int firstDigit = num;
        while (firstDigit >= 10) {
            firstDigit /= 10;
        }
        int lastDigit = num % 10;

        return isOdd(firstDigit) && isOdd(lastDigit);
    }

    private boolean isOdd(int num) {
        return num % 2 != 0;
    }
}

