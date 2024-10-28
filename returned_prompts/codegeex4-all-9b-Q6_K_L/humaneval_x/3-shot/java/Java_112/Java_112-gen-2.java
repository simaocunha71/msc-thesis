        StringBuilder result = new StringBuilder();
        for (char ch : s.toCharArray()) {
            if (c.indexOf(ch) == -1) {
                result.append(ch);
            }
        }
        boolean isPalindrome = result.toString().equals(result.reverse().toString());
        return Arrays.asList(result.toString(), isPalindrome);
    }
}

