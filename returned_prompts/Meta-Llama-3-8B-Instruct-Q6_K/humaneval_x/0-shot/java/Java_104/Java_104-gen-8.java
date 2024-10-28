    public List<Integer> uniqueDigits(List<Integer> x) {
        List<Integer> result = new ArrayList<>();
        for (int num : x) {
            if (!hasEvenDigit(num)) {
                result.add(num);
            }
        }
        Collections.sort(result);
        return result;
    }

    private boolean hasEvenDigit(int num) {
        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                return true;
            }
            num /= 10;
        }
        return false;
    }
}
