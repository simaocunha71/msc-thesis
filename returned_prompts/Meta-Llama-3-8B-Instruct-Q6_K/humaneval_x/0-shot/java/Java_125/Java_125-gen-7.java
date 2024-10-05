    public Object splitWords(String txt) {
        List<String> result = new ArrayList<>();
        String[] words = txt.split("\\s+");
        if (words.length == 0) {
            words = txt.split(",");
            if (words.length == 0) {
                int count = 0;
                for (char c : txt.toLowerCase().toCharArray()) {
                    if (c >= 'a' && c <= 'z' && (c - 'a') % 2 == 1) {
                        count++;
                    }
                }
                return count;
            }
        }
        for (String word : words) {
            result.add(word.trim());
        }
        return result;
    } 





