        if (isPalindrome(string)) {
            return string;
        }

        int i = string.length() - 1;
        while (i > 0) {
            if (isPalindrome(string.substring(0, i))) {
                return string.substring(0, i) + new StringBuilder(string.substring(i)).reverse().toString();
            }
            i--;
        }
        return "";
    }
}

