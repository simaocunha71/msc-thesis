        int len = word.length();
        for (int i = 0; i < len; i++) {
            if (word.charAt(i) == 'a' || word.charAt(i) == 'e' || word.charAt(i) == 'i' || word.charAt(i) == 'o' || word.charAt(i) == 'u') {
                if (i > 0 && word.charAt(i - 1) != 'a' && word.charAt(i - 1) != 'e' && word.charAt(i - 1) != 'i' && word.charAt(i - 1) != 'o' && word.charAt(i - 1) != 'u') {
                    if (i + 1 < len && word.charAt(i + 1) != 'a' && word.charAt(i + 1) != 'e' && word.charAt(i + 1) != 'i' && word.charAt(i + 1) != 'o' && word.charAt(i + 1) != 'u') {
                        return String.valueOf(word.charAt(i));
                    }
                }
            }
        }
        return "";
    }
}

