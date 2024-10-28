        List<Integer> res = new ArrayList<>(Arrays.asList(0, 0));
        for (int i = 1; i <= n; i++) {
            if (isPalindrome(i)) {
                if (i % 2 == 0) {
                    res.set(0, res.get(0) + 1);
                } else {
                    res.set(1, res.get(1) + 1);
                }
            }
        }
        return res;
    }

    private boolean isPalindrome(int n) {
        String str = String.valueOf(n);
        int i = 0;
        int j = str.length() - 1;
        while (i < j) {
            if (str.charAt(i++) != str.charAt(j--)) {
                return false;
            }
        }
        return true;
    }
}

