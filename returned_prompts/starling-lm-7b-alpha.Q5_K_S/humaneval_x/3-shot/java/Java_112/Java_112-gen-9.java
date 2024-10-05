        List<Object> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for (char ch : s.toCharArray()) {
            if (!c.contains("" + ch)) {
                sb.append(ch);
            }
        }
        result.add(sb.toString());
        result.add(isPalindrome(sb.toString()));
        return result;
    }

    public boolean isPalindrome(String s) {
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != s.charAt(s.length() - i - 1)) {
                return false;
            }
        }
        return true;
    }
}

