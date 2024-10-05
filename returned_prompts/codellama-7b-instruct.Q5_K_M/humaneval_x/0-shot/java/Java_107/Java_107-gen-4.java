        List<Integer> result = new ArrayList<Integer>();
        int even = 0, odd = 0;
        for (int i = 1; i <= n; i++) {
            if (isPalindrome(i) && isEven(i)) {
                even++;
            }
            if (isPalindrome(i) && isOdd(i)) {
                odd++;
            }
        }
        result.add(even);
        result.add(odd);
        return result;
    }
    public boolean isEven(int n) {
        if (n == 0) {
            return true;
        }
        return false;
    }

    public boolean isOdd(int n) {
        if (n == 0) {
            return false;
        }
        return true;
    }

    public boolean isPalindrome(int n) {
        int rev = 0;
        int origin = n;
        while (n != 0) {
            rev = rev * 10 + n % 10;
            n = n / 10;
        }
        if (rev == origin) {
            return true;
        } else {
            return false;
        }
    }
}
