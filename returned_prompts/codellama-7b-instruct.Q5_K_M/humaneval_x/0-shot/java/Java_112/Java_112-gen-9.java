        List<Object> result = new ArrayList<Object>();
        String resultString = new String();
        boolean isPalindrome = false;

        // Check if the string is palindrome
        if (s.equals(new StringBuilder(s).reverse().toString())) {
            isPalindrome = true;
        }
        else {
            isPalindrome = false;
        }

        // Delete all characters in s that are equal to any character in c
        if (s.contains(c)) {
            for (int i = 0; i < s.length(); i++) {
                if (!c.contains(s.charAt(i) + "")) {
                    resultString += s.charAt(i);
                }
            }
        }
        else {
            resultString = s;
        }

        // Check if the result string is palindrome
        if (resultString.equals(new StringBuilder(resultString).reverse().toString())) {
            isPalindrome = true;
        }
        else {
            isPalindrome = false;
        }

        result.add(resultString);
        result.add(isPalindrome);
        return result;
    }
}

