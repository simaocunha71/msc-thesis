    public Object splitWords(String txt) {
        String[] words = txt.split("\\s+");
        if (words.length == 0) {
            return txt.replace(",", "").codePoints().filter(c -> c >= 'a' && c <= 'z').filter(c -> (c - 'a') % 2 != 0).count();
        } else {
            return Arrays.asList(words);
        }
    }   


