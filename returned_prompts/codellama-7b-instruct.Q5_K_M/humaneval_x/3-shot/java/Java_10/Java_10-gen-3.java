        if (isPalindrome(string)) return string;

        int i = string.length() - 1;
        while (i >= 0 && !isPalindrome(string.substring(0, i + 1))) {
            i--;
        }
        return string.substring(0, i + 1) + new StringBuilder(string.substring(0, i + 1)).reverse().toString();
    }
}

