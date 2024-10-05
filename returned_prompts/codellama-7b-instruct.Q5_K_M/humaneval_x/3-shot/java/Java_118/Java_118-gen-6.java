        if (word.length() < 3) return "";

        for (int i = word.length() - 1; i >= 0; i--) {
            if (word.charAt(i) == 'a' || word.charAt(i) == 'e' || word.charAt(i) == 'i' || word.charAt(i) == 'o' || word.charAt(i) == 'u') {
                if (i < word.length() - 1 && word.charAt(i + 1) != word.charAt(i)) {
                    return String.valueOf(word.charAt(i));
                }
            }
        }
        return "";
    }
}

