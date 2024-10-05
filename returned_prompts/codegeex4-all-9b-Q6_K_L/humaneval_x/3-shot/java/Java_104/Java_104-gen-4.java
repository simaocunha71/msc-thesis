        List<Integer> result = new ArrayList<>();
        for (int n : x) {
            if (isUniqueDigits(n)) {
                result.add(n);
            }
        }
        Collections.sort(result);
        return result;
    }

    private boolean isUniqueDigits(int n) {
        boolean[] digits = new boolean[10];
        while (n > 0) {
            int digit = n % 10;
            if (digits[digit]) {
                return false;
            }
            digits[digit] = true;
            n = n / 10;
        }
        return true;
    }
}

