        List<Object> result = new ArrayList<>();
        String newString = "";
        boolean isPalindrome = true;
        for (int i = 0; i < s.length(); i++) {
            if (!c.contains(String.valueOf(s.charAt(i)))) {
                newString = newString + s.charAt(i);
            } else {
                isPalindrome = false;
            }
        }
        int j = 0;
        while (j < newString.length() && j < c.length()) {
            if (newString.charAt(j) == c.charAt(j)) {
                j++;
            } else {
                isPalindrome = false;
                j = newString.length();
            }
        }
        result.add(newString);
        result.add(isPalindrome);
        return result;
    }
}

