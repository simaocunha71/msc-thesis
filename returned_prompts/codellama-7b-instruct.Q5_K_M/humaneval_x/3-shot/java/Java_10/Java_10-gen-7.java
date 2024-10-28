        if (isPalindrome(string)) return string;

        for (int i = string.length(); i > 0; i--) {
            String postfix = string.substring(i);
            if (isPalindrome(postfix)) {
                return string + new StringBuilder(postfix).reverse().toString();
            }
        }
        return "";
    }
}

