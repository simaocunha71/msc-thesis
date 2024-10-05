        int i = string.length() - 1;
        while (i >= 0 && !isPalindrome(string.substring(0, i + 1))) {
            i -= 1;
        }
        return string + string.substring(0, i + 1).reverse();
    }
}

