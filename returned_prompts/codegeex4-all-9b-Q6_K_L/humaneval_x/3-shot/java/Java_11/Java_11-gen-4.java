        StringBuilder result = new StringBuilder();
        int maxLength = Math.max(a.length(), b.length());

        for (int i = 0; i < maxLength; i++) {
            char aChar = i < a.length() ? a.charAt(i) : '0';
            char bChar = i < b.length() ? b.charAt(i) : '0';

            if (aChar == bChar) {
                result.append('0');
            } else {
                result.append('1');
            }
        }
        return result.toString();
    }
}

