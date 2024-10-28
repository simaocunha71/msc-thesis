        int i = string.length() - 1;
        int j = 0;
        while (i >= j && isPalindrome(string.substring(j, i + 1))) {
            i--;
            j++;
        }
        String postfix = string.substring(j);
        String prefix = "";
        for (i = string.length() - 1; i >= j; i--) {
            prefix = string.charAt(i) + prefix;
        }
        return prefix + postfix;
    }
}


