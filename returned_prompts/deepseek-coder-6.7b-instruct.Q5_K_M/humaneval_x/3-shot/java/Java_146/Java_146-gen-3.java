        int count = 0;
        for (int num : nums) {
            if (num > 10) {
                int firstDigit = Math.abs(num / 10);
                int lastDigit = Math.abs(num % 10);
                if (firstDigit % 2 != 0 && lastDigit % 2 != 0) {
                    count++;
                }
            }
        }
        return count;
    }
}

