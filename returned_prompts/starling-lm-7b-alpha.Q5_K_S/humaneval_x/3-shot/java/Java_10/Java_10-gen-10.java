        String result = string + string;
        String reversed_prefix = string.substring(0, string.length() / 2);
        String suffix = string.substring(string.length() / 2);
        while (!isPalindrome(suffix)) {
            suffix = suffix.substring(0, suffix.length() - 1);
        }
        result = result.substring(0, result.length() - reversed_prefix.length()) + suffix + reversed_prefix;
        return result;
    }
}


