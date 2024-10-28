        List<Object> result = new ArrayList<>();
        StringBuilder str = new StringBuilder(s);
        for (char ch : c.toCharArray()) {
            while (str.indexOf(ch) != -1) {
                str.deleteCharAt(str.indexOf(ch));
            }
        }
        result.add(str.toString());
        result.add(isPalindrome(str.toString()));
        return result;
    }

    public boolean isPalindrome(String str) {
        int length = str.length();
        for (int i = 0; i < length / 2; i++) {
            if (str.charAt(i) != str.charAt(length - 1 - i)) {
                return false;
            }
        }
        return true;
    }
}

