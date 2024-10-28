        int count = 0;
        for (Integer num : nums) {
            if (num > 10) {
                int lastDigit = Math.abs(num % 10);
                int firstDigit = Math.abs(num / 10);
                if (lastDigit % 2 != 0 && firstDigit % 2 != 0) {
                    count++;
                }
            }
        }
        return count;
    }
}

