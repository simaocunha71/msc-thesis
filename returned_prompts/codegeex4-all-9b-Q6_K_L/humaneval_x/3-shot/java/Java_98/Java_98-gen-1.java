        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (i % 2 == 0 && isUpperVowel(s.charAt(i))) count += 1;
        }
        return count;

    }

    private boolean isUpperVowel(char c) {
        return c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U';
    }
}

