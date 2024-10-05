        if (isPalindrome(string)) {
            return string;
        }

        int i = 0;
        int j = string.length() - 1;

        while (i < j) {
            if (string.charAt(i) != string.charAt(j)) {
                j--;
                continue;
            }
            i++;
            j--;
        }
        StringBuilder prefix = new StringBuilder();
        StringBuilder postfix = new StringBuilder();
        for (; i < string.length(); i++) {
            prefix.append(string.charAt(i));
        }
        for (; j >= 0; j--) {
            postfix.append(string.charAt(j));
        }
        return prefix + postfix.reverse().toString();
    }
}

