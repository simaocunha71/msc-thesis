        String result = string + string;
        while (!isPalindrome(result)) {
            int i = result.length() - 1;
            while (!isPalindrome(result.substring(0, i))) {
                i--;
            }
            result = result.substring(0, i) + result.substring(result.length() - i, result.length());
        }
        return result.substring(string.length());
    }
}

