        int count = 0;
        for (int num : nums) {
            if (num > 10 && isOdd(num)) {
                count++;
            }
        }
        return count;
    }

    private boolean isOdd(int num) {
        int firstDigit = Math.abs(num) / 10;
        int lastDigit = Math.abs(num) % 10;
        return firstDigit % 2 != 0 && lastDigit % 2 != 0;
    }
}

