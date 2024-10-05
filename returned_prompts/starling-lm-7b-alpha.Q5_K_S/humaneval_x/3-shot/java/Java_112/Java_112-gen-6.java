        StringBuilder stringBuilder = new StringBuilder(s);

        for (char ch : c.toCharArray()) {
            while (stringBuilder.indexOf(String.valueOf(ch)) >= 0) {
                stringBuilder.deleteCharAt(stringBuilder.indexOf(String.valueOf(ch)));
            }
        }

        String result = stringBuilder.toString();
        return Arrays.asList(result, isPalindrome(result));
    }

    private boolean isPalindrome(String str) {
        for (int i = 0; i < str.length() / 2; i++) {
            if (str.charAt(i) != str.charAt(str.length() - 1 - i)) {
                return false;
            }
        }
        return true;
    }
}

