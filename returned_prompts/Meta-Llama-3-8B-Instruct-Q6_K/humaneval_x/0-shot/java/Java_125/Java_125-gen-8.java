    public Object splitWords(String txt) {
        String[] words = txt.split("\\s+"); //split on whitespace
        if (words.length == 0) {
            words = txt.split(",");
            if (words.length == 0) {
                int count = 0;
                for (char c : txt.toCharArray()) {
                    if (Character.isLowerCase(c) && (c - 'a') % 2 == 1) {
                        count++;
                    }
                }
                return count;
            }
        }
        return Arrays.asList(words);
    }