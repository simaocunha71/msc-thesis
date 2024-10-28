    public int countNums(List<Integer> arr) {
        int count = 0;
        for (int num : arr) {
            int sum = getSumOfDigits(num);
            if (sum > 0) {
                count++;
            }
        }
        return count;
    }

    private int getSumOfDigits(int num) {
        int sum = 0;
        while (num != 0) {
            int digit = Math.abs(num % 10);
            sum += digit;
            num /= 10;
        }
        return sum;
    }
}
