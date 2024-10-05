public List<Integer> uniqueDigits(List<Integer> x) {
    Set<Integer> res = new HashSet<>();
    for (int num : x) {
        boolean hasEvenDigit = false;
        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                hasEvenDigit = true;
                break;
            }
            num /= 10;
        }
        if (!hasEvenDigit) {
            res.add(num);
        }
    }
    return new ArrayList<>(res);
}