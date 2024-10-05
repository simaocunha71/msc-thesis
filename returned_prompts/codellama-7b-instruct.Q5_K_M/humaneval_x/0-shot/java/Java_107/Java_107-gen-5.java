        List<Integer> ans = new ArrayList();
        int countEven = 0;
        int countOdd = 0;
        for (int i = 1; i < n; i++) {
            String str = Integer.toString(i);
            if (isPalindrome(str)) {
                if (isEven(str)) {
                    countEven++;
                } else {
                    countOdd++;
                }
            }
        }
        ans.add(countEven);
        ans.add(countOdd);
        return ans;
    }

    public boolean isPalindrome(String str) {
        if (str.length() == 0) {
            return true;
        }
        for (int i = 0; i < str.length() / 2; i++) {
            if (str.charAt(i) != str.charAt(str.length() - 1 - i)) {
                return false;
            }
        }
        return true;
    }

    public boolean isEven(String str) {
        int sum = 0;
        for (char c : str.toCharArray()) {
            sum += c - '0';
        }
        return sum % 2 == 0;
    }
}

