        int i = string.length() - 1;
        while (i >= 0) {
            if (isPalindrome(string.substring(0, i + 1))) {
                break;
            }
            i--;
        }
        return string + new StringBuilder(string.substring(0, i + 1)).reverse().toString();
    }
}

