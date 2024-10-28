        String maxWord = "";
        int maxUniqueChars = 0;

        for (String word : words) {
            Set<Character> uniqueChars = new HashSet<>();
            for (char c : word.toCharArray()) {
                uniqueChars.add(c);
            }

            if (uniqueChars.size() > maxUniqueChars) {
                maxWord = word;
                maxUniqueChars = uniqueChars.size();
            }
        }
        return maxWord;
    }
}

