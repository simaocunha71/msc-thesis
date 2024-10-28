        String result = string;
        while (!isPalindrome(result)) {
            int i = 0;
            while (result.charAt(i) == result.charAt(result.length() - i - 1)) {
                i++;
            }
           