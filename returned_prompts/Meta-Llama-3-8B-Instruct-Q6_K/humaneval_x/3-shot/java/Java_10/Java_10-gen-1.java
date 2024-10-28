        if (isPalindrome(string)) {
            return string;
        }

        for (int i = string.length() - 1; i >= 0; i--) {
            String prefix = string.substring(0, i + 1);
            String postfix = string.substring(i);
            if (isPalindrome(postfix)) {
                return prefix + new StringBuilder(postfix).reverse().toString();
            }
        }
        return string;
    }
}

