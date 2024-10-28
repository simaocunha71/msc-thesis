        int result = 0;
        for (int start = 0; start < string.length(); start++) {
            int length = 0;
            while (length < substring.length() && start + length < string.length() && string.charAt(start + length) == substring.charAt(length)) {
                length += 1;
            }
            if (length == substring.length()) {
                result += 1;
            }
        }
        return result;
    }
}

