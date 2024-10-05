        for (int i = word.length() - 1; i > 0; i--) {
            if (isVowel(word.charAt(i))) {
                return String.valueOf(word.charAt(i));
            }
        }
        return "";
    }

    private boolean isVowel(char c) {
        return "aeiouAEIOU".indexOf(c) != -1;
    }
}

