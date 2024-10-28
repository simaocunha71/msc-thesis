        StringBuilder result = new StringBuilder();
        for (int i = word.length() - 1; i > 0; i--) {
            char c = word.charAt(i);
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
                if (Character.isLetter(word.charAt(i - 1)) && !Character.isLetter(word.charAt(i + 1))) {
                    return String.valueOf(c);
                }
            }
        }
        return "";
    }
}

