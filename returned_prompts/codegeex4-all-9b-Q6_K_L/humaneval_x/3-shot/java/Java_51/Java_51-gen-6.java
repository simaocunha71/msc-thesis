        String result = "";
        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            if (!isVowel(c)) {
                result += c;
            }
        }
        return result;
    }

    private boolean isVowel(char c) {
        c = Character.toLowerCase(c);
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}

