        List<String> words = new ArrayList<>();
        boolean first = true;
        for (char c : txt.toCharArray()) {
            if (c == ' ' || c == ',') {
                if (!first) {
                    words.add(String.valueOf(c));
                }
                first = true;
            } else if (Character.isLetter(c)) {
                if (Character.toLowerCase(c) == c) {
                    if ((c - 'a') % 2 == 1) {
                        words.add(String.valueOf(c));
                    }
                } else {
                    words.add(String.valueOf(c).toLowerCase());
                }
            }
        }
        if (words.isEmpty()) {
            return txt.chars().filter(c -> c == 'a' || c == 'b' || c == 'd' || c == 'f').count();
        } else {
            return words;
        }
    }
}

