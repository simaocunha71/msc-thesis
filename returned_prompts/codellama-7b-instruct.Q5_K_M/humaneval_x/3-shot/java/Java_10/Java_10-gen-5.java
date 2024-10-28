        if (isPalindrome(string)) return string;

        StringBuilder postfix = new StringBuilder();
        for (int i = string.length() - 1; i >= 0; i--) {
            if (isPalindrome(string.substring(0, i + 1))) {
                postfix = new StringBuilder(string.substring(i));
                break;
            }
        }

        StringBuilder prefix = new StringBuilder();
        for (int i = 0; i < string.length(); i++) {
            if (isPalindrome(string.substring(i))) {
                prefix = new StringBuilder(string.substring(0, i));
                break;
            }
        }

        return string.concat(prefix.reverse().toString());
    }
}

