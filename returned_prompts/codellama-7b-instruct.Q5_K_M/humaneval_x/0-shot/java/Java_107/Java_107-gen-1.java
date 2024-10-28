        List<Integer> res = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            String num = Integer.toString(i);
            if (isPalindrome(num)) {
                if (isEven(num)) {
                    res.add(0, 1);
                } else {
                    res.add(1, 1);
                }
            }
        }
        return res;
    }

    private boolean isPalindrome(String num) {
        int left = 0;
        int right = num.length() - 1;
        while (left < right) {
            if (num.charAt(left) != num.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    private boolean isEven(String num) {
        return Integer.parseInt(num) % 2 == 0;
    }
}
