        StringBuilder sb = new StringBuilder();
        boolean vowel = false;
        for (char c : text.toCharArray()) {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
                vowel = true;
                continue;
            }
            if (!vowel) sb.append(c);
            vowel = false;
        }
        return sb.toString();
    }
}

