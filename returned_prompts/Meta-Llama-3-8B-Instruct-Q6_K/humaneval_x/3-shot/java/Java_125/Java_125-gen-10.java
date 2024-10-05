        String[] words = txt.split("\\s+");
        if (words.length == 1 && !words[0].contains(",")) {
            int count = 0;
            for (char c : words[0].toCharArray()) {
                if (Character.isLowerCase(c) && (c - 'a') % 2 == 1) {
                    count++;
                }
            }
            return count;
        } else {
            return Arrays.asList(words);
        }
    }
}

