        if (isPalindrome(string)) {
            return string;
        }
        int j = string.length() - 1;
        int i = 0;
        while (i < j) {
            if (isPalindrome(string.substring(i, j+1))) {
                break;
            }
            j--;
        }
        return string.substring(0, j+1) + new StringBuilder(string.substring(0, j+1)).reverse().toString();
    }
}

