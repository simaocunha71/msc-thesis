        int count = 0;
        for (int num : nums) {
            if (num > 10 && isOddFirstAndLast(num)) {
                count++;
            }
        }
        return count;

    }

    private boolean isOddFirstAndLast(int num) {
        int firstDigit = num / 10;
        int lastDigit = num % 10;
        return firstDigit % 2 != 0 && lastDigit % 2 != 0;
    }
}