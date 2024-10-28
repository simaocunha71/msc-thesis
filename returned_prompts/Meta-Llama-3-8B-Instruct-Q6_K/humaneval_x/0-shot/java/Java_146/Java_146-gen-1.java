public int specialFilter(List<Integer> nums) {
    int count = 0;
    for (int num : nums) {
        if (num > 10 && isOddFirstAndLastDigit(num)) {
            count++;
        }
    }
    return count;
}

public boolean isOddFirstAndLastDigit(int num) {
    String str = String.valueOf(num);
    return str.charAt(0) % 2 != 0 && str.charAt(str.length() - 1) % 2 != 0;
}