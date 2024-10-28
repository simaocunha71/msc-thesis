        int length = word.length();

        for (int i = length - 1; i > 0; i--) {
            char current_char = word.charAt(i);
            char previous_char = word.charAt(i - 1);

            if (isVowel(current_char) && !isVowel(previous_char)) {
                return String.valueOf(current_char);
            }
        }

        return "";
    }

    private boolean isVowel(char c) {
        return (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U');
    }
}

