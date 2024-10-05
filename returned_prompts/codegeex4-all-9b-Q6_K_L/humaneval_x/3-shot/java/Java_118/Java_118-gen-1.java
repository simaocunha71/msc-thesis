        for (int i = word.length() - 1; i >= 0; i--) {
            char c = word.charAt(i);
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                if (i == 0 || i == word.length() - 1) {
                    return "";
                } else {
                    return String.valueOf(word.charAt(i));
                }
            }
        }
        return "";
    }
}

