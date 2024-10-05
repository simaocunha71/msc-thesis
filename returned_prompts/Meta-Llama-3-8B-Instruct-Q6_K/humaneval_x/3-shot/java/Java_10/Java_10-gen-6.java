        if (isPalindrome(string)) return string;

        for (int length = 1; length <= string.length(); length++) {
            String prefix = string.substring(0, length);
            String postfix = string.substring(length);

            if (isPalindrome(postfix)) {
                return prefix + postfix + new StringBuilder(prefix).reverse().toString();
            }
        }
        return string;
    }
} 