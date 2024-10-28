        StringBuilder sb = new StringBuilder(s);
        for (char ch : c.toCharArray()) {
            while (sb.indexOf(String.valueOf(ch)) != -1) {
                sb.deleteCharAt(sb.indexOf(String.valueOf(ch)));
            }
        }
        int length = sb.length();
        boolean isPalindrome = true;
        for (int i = 0; i < length; i++) {
            if (sb.charAt(i) != sb.charAt(length - i - 1)) {
                isPalindrome = false;
                break;
            }
        }

        return Arrays.asList(sb.toString(), isPalindrome);
    }
}

