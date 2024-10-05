        List<Object> result = new ArrayList<>();
        String newStr = "";
        for (char c1 : s.toCharArray()) {
            if (!c.contains(String.valueOf(c1))) {
                newStr += c1;
            }
        }
        result.add(newStr);
        result.add(isPalindrome(newStr));
        return result;
    }

    private boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}