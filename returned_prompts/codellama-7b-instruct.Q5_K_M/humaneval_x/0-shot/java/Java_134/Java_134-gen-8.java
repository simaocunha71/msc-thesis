        boolean result = false;
        int lastCharIndex = txt.length() - 1;
        char lastChar = txt.charAt(lastCharIndex);
        if (Character.isLetter(lastChar)) {
            // check if the last char is part of a word
            String[] words = txt.split(" ");
            for (int i = 0; i < words.length; i++) {
                if (lastCharIndex >= words[i].length()) {
                    lastCharIndex -= words[i].length() + 1;
                } else {
                    result = false;
                    break A;
                }
            }
            result = true;
        }
        return result;
    }
}
