    public int specialFilter(List<Integer> nums) {
        int count = 0;
        for (Integer num : nums) {
            if (Math.abs(num) > 10 && (num % 10) % 2 != 0 && (num / 10) % 10 % 2 != 0) {
                count++;
            }
        }
        return count;
    }