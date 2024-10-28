        String[] words = txt.split("\\s+"); // split on whitespace
        if (words.length == 1 && !words[0].contains(",")) {
            int count = 0;
            for (char c : words[0].toLowerCase().toCharArray()) {
                if (c >= 'a' && c <= 'z' && (c - 'a') % 2 == 1) {
                    count++;
                }
            }
            return count;
        }
        return Arrays.asList(words);
    }
}

