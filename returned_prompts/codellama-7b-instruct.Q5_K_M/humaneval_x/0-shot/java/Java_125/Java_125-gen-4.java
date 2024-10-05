        List<String> result = new ArrayList<String>();
        if (txt.contains(" ")) {
            String[] words = txt.split(" ");
            for (String word : words) {
                result.add(word);
            }
        } else if (txt.contains(",")) {
            String[] words = txt.split(",");
            for (String word : words) {
                result.add(word);
            }
        } else {
            for (int i = 0; i < 26; i++) {
                if ((txt.charAt(i) >= 'a' && txt.charAt(i) <= 'z') && (i % 2 == 0)) {
                    result.add(txt.substring(i, i + 1));
                }
            }
        }
        return result;
    }
}

