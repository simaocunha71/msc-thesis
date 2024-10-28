        String[] words = txt.split("[ ,]+");
        if (words.length == 1) {
            int count = 0;
            for (int i = 0; i < txt.length(); i++) {
                if ((txt.charAt(i) >= 'a' && txt.charAt(i) <= 'z') && (i % 2 != 0)) {
                    count++;
                }
            }
            return count;
        } else {
            return Arrays.asList(words);
        }
    }
}

