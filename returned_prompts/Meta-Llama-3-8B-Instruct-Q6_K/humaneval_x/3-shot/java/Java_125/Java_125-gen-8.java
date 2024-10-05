        String[] words = txt.split("\\s+");
        if (words.length == 1 && words[0].indexOf(',') != -1) {
            return countOddLetters(txt);
        } else {
            return Arrays.asList(words);
        }
    }

    private int countOddLetters(String txt) {
        int count = 0;
        for (char c : txt.toLowerCase().toCharArray()) {
            if (c >= 'a' && c <= 'z' && (c - 'a') % 2 != 0) {
                count++;
            }
        }
        return count;
    }
}
