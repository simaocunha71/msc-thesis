public int specialFilter(List<Integer> nums) {
    int count = 0;
    for (Integer num : nums) {
        if (Math.abs(num) > 10 && isOddFirstAndLastDigit(num)) {
            count++;
        }
    }
    return count;
}

private boolean isOddFirstAndLastDigit(int num) {
    int firstDigit = num / 10;
    int lastDigit = num % 10;
    return (firstDigit % 2 != 0) && (lastDigit % 2 != 0);
}  