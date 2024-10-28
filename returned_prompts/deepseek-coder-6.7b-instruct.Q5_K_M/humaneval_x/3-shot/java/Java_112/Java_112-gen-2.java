        StringBuilder sb = new StringBuilder();
        boolean isPalindrome = true;

        for (char ch : s.toCharArray()) {
            if (!c.contains(String.valueOf(ch))) {
                sb.append(ch);
            }
        }

        String result = sb.toString();
        int length = result.length();

        for (int i = 0; i < length / 2; i++) {
            if (result.charAt(i) != result.charAt(length - i - 1)) {
                isPalindrome = false;
                break;
            }
        }

        return Arrays.asList(result, isPalindrome);
    }
}

