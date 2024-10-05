    public String findMax(List<String> words) {
        if (words.isEmpty()) {
            return "";
        }

        String maxWord = words.get(0);
        int maxUniqueChars = 0;

        for (String word : words) {
            Set<Character> uniqueChars = new HashSet<>();
            for (char c : word.toCharArray()) {
                uniqueChars.add(c);
            }

            if (uniqueChars.size() > maxUniqueChars) {
                maxUniqueChars = uniqueChars.size();
                maxWord = word;
            } else if (uniqueChars.size() == maxUniqueChars) {
                if (word.compareTo(maxWord) < 0) {
                    maxWord = word;
                }
            }
        }

        return maxWord;
    }