        if (isPalindrome(string)) return string;
        // find longest postfix that is palindrome
        int i = string.length() - 1;
        while (i >= 0 && !isPalindrome(string.substring(i))) {
            i--;
        }
        // append prefix from before the palindrome
        // suffix
        return string.substring(0, i + 1) + new StringBuilder(string.substring(i + 1)).reverse().toString();
    }
}

