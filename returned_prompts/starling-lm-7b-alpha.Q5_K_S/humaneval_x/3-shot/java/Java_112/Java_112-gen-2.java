        List<Object> result = new ArrayList<>();
        StringBuilder string_builder = new StringBuilder(s);
        for (char ch : c.toCharArray()) {
            for (int i = 0; i < string_builder.length(); i++) {
                if (string_builder.charAt(i) == ch) {
                    string_builder.deleteCharAt(i);
                    break;
                }
            }
        }
        result.add(string_builder.toString());
        result.add(isPalindrome(string_builder.toString()));
        return result;
    }

    public boolean isPalindrome(String s) {
        for (int i = 0; i < s.length() / 2; i++) {
            if (s.charAt(i) != s.charAt(s.length() - i - 1)) return false;
        }
        return true;
    }
}


