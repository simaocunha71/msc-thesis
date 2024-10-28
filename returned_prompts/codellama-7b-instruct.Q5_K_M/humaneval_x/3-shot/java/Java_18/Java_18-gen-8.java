        int result = 0;
        int substring_length = substring.length();
        for (int i = 0; i <= string.length() - substring_length; i++) {
            if (string.substring(i, i + substring_length).equals(substring)) {
                result += 1;
            }
        }
        return result;
    }
}

