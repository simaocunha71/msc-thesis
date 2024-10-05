        String longest_postfix = "";
        String longest_prefix = "";
        for (int i = 0; i < string.length(); i++) {
            if (isPalindrome(string.substring(i))) {
                longest_postfix = string.substring(i);
            }
        }
        for (int j = 0; j < string.length(); j++) {
            String prefix = string.substring(0, j);
            if (isPalindrome(prefix)) {
                longest_prefix = prefix;
            }
        }
        return longest_prefix + new StringBuilder(longest_postfix).reverse().toString();
    }
}

