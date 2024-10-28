        List<Integer> result = new ArrayList<>(Arrays.asList(0, 0));
        for (int i = 1; i <= n; i++) {
            if (isPalindrome(String.valueOf(i))) {
                if (i % 2 == 0) {
                    result.set(0, result.get(0) + 1);
                } else {
                    result.set(1, result.get(1) + 1);
                }
            }
        }
        return result;
    }

    private boolean isPalindrome(String s) {
        int start = 0;
        int end = s.length() - 1;
        while (start < end) {
            if (s.charAt(start) != s.charAt(end)) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
}

