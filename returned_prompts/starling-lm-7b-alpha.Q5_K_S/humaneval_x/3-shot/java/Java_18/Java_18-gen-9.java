        int result = 0;
        for (int i = 0; i + substring.length() <= string.length(); i++) {
            if (string.substring(i, i + substring.length()).equals(substring)) {
                result += 1;
            }
        }
        return result;
    }
}

