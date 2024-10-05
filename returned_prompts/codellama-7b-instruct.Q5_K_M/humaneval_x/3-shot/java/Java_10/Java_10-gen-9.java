        if (isPalindrome(string)) return string;

        int max_postfix_length = 0;
        String longest_postfix = "";
        for (int i = string.length() - 1; i >= 0; i--) {
            String postfix = string.substring(i);
            if (isPalindrome(postfix) && postfix.length() > max_postfix_length) {
                max_postfix_length = postfix.length();
                longest_postfix = postfix;
            }
        }

        String prefix = string.substring(0, string.length() - max_postfix_length);
        return prefix + new StringBuilder(longest_postfix).reverse().toString();
    }
}

