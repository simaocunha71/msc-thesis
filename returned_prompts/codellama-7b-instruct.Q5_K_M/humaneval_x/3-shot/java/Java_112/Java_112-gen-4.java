        List<Object> result = new ArrayList<>();

        // Step 1: delete all the characters in s that are equal to any character in c
        StringBuilder new_string = new StringBuilder();
        for (char ch : s.toCharArray()) {
            if (c.indexOf(ch) == -1) {
                new_string.append(ch);
            }
        }

        // Step 2: Check if the result string is palindrome
        String check_string = new_string.toString();
        int length = check_string.length();
        for (int i = 0; i < length / 2; i++) {
            if (check_string.charAt(i) != check_string.charAt(length - i - 1)) {
                result.add(new_string.toString());
                result.add(false);
                return result;
            }
        }
        result.add(new_string.toString());
        result.add(true);
        return result;
    }
}

