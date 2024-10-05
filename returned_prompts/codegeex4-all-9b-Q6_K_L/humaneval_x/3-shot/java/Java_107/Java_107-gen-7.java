        int even_count = 0;
        int odd_count = 0;
        for (int i = 1; i <= n; i++) {
            if (isPalindrome(i)) {
                if (i % 2 == 0) {
                    even_count += 1;
                } else {
                    odd_count += 1;
                }
            }
        }
        return Arrays.asList(even_count, odd_count);
    }

    public boolean isPalindrome(int number) {
        String str = Integer.toString(number);
        int left = 0;
        int right = str.length() - 1;
        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) return false;
            left += 1;
            right -= 1;
        }
        return true;
    }
}

