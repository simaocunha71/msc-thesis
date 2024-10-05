    public Object splitWords(String txt) {
        List<String> result = new ArrayList<>();
        String[] words = txt.split("\\s+");

        for (String word : words) {
            if (word.contains(",")) {
                words = word.split(",");
                for (String w : words) {
                    result.add(w.trim());
                }
            } else {
                result.add(word);
            }
        }

        if (result.isEmpty()) {
            int count = 0;
            for (char c : txt.toLowerCase().toCharArray()) {
                if (c >= 'a' && c <= 'z' && (c - 'a') % 2 != 0) {
                    count++;
                }
            }
            return count;
        }

        return result;
    }