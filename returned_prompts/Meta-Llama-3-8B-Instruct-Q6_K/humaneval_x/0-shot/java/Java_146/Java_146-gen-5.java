    public int specialFilter(List<Integer> nums) {
        int count = 0;
        for (int num : nums) {
            if (Math.abs(num) > 10) {
                int firstDigit = num / 10;
                int lastDigit = Math.abs(num) % 10;
                if (firstDigit % 2 != 0 && lastDigit % 2 != 0) {
                    count++;
                }
            }
        }
        return count;
    }