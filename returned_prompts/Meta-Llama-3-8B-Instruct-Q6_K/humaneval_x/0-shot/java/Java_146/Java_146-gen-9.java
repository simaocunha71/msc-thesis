    public int specialFilter(List<Integer> nums) {
        int count = 0;
        for (int num : nums) {
            if (num > 10) {
                int firstDigit = num / 10;
                int lastDigit = num % 10;
                if (firstDigit % 2 == 1 && lastDigit % 2 == 1) {
                    count++;
                }
            }
        }
        return count;
    }