        List<String> result = new ArrayList<>();
        int current_count = 0;
        StringBuilder current_word = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (c == ' ') {
                if (current_count == n) result.add(current_word.toString());
                current_word.setLength(0);
                current_count = 0;
            } else if (!isVowel(c)) current_count += 1;
            else current_word.append(c);
        }
        if (current_count == n) result.add(current_word.toString());
        return result;
    }

    public boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
            || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U';
    }
}

