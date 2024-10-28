        String[] words = txt.split(" ");
        if (words.length > 0) {
            return Arrays.asList(words);
        }
        if (txt.contains(",")) {
            return txt.split(",");
        }
        int result = 0;
        for (int i = 0; i < txt.length(); i++) {
            char c = txt.charAt(i);
            if ('a' <= c && c <= 'z') {
                int ord = c - 'a';
                if (ord % 2 == 1) {
                    result += 1;
                }
            }
        }
        return result;
    }
}

