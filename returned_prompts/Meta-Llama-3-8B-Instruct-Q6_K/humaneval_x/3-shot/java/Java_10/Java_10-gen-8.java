        String original = string;
        for (int i = string.length() - 1; i >= 0; i--) {
            String suffix = string.substring(i);
            if (isPalindrome(suffix)) {
                return original + new StringBuilder(suffix).reverse().toString();
            }
        }
        return original;
    }
}

