        StringBuilder result = new StringBuilder();
        for (char c1 : s.toCharArray()) {
            if (!c.contains(String.valueOf(c1))) {
                result.append(c1);
            }
        }
        return new ArrayList<>(Arrays.asList(result.toString(), isPalindrome(result.toString())));
    }

    public boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) return false;
            left++;
            right--;
        }
        return true;
    }
}

