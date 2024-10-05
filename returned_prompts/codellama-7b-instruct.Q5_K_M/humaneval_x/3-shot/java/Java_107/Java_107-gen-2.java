        List<Integer> result = new ArrayList<>();
        int count_even = 0;
        int count_odd = 0;

        for (int i = 1; i < n; i++) {
            String string_i = String.valueOf(i);
            if (isPalindrome(string_i) && isEven(i)) {
                count_even += 1;
            }
            if (isPalindrome(string_i) && isOdd(i)) {
                count_odd += 1;
            }
        }
        result.add(count_even);
        result.add(count_odd);
        return result;
    }

    // helper functions
    private boolean isPalindrome(String s) {
        if (s.length() == 1) return true;
        for (int i = 0; i < s.length() / 2; i++) {
            if (s.charAt(i) != s.charAt(s.length() - 1 - i)) return false;
        }
        return true;
    }
    private boolean isEven(int x) {
        return x % 2 == 0;
    }
    private boolean isOdd(int x) {
        return !isEven(x);
    }
}

