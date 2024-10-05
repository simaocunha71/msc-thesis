        String result = string;
        String prefix = string.substring(0, string.length() / 2 + 1);
        String suffix = string.substring(string.length() / 2);
        while (!isPalindrome(suffix)) {
            suffix = suffix.substring(0, suffix.length() - 1);
        }
        result = result.substring(0, result.length() - suffix.length())
                + suffix + result.substring(result.length() - suffix.length());
        return result;
    }
}


```