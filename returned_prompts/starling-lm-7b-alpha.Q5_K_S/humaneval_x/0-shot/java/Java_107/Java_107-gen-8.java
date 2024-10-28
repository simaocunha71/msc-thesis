        List<Integer> res = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            String s = i + "";
            if (isPalindrome(s)) {
                if (s.length() % 2 == 0) {
                    res.add(1);
                } else {
                    res.add(0);
                }
            }
        }
        int even = 0, odd = 0;
        for (int i : res) {
            if (i == 1) {
                even++;
            } else {
                odd++;
            }
        }
        res.set(0, even);
        res.set(1, odd);
        return res;
    }

    public boolean isPalindrome(String s) {
        int l = 0;
        int r = s.length() - 1;
        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}













































































































































































































































