        StringBuilder builder = new StringBuilder(string);
        builder.reverse();
        String reversed = builder.toString();
        String suffix = string;
        while (isPalindrome(suffix)) {
            suffix = suffix.substring(0, suffix.length() - 1);
        }
        String prefix = string.substring(0, string.length() - suffix.length());
        return prefix + suffix + reversed.substring(0, suffix.length());
    }
}

