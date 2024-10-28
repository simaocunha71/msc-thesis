        List<Integer> result = new ArrayList<>();
        int count = 0;
        for (int i = 1; i <= n; i++) {
            if (isPalindrome(i)) {
                if (i % 2 == 0) count += 1;
                else result.add(1);
            }
        }
        result.add(count);
        return result;
    }

    boolean isPalindrome(int num) {
        String str = String.valueOf(num);
        int start = 0;
        int end = str.length() - 1;

        while (start < end) {
            if (str.charAt(start) != str.charAt(end)) {
                return false;
            }
            start += 1;
            end -= 1;
        }
        return true;
    }
}

