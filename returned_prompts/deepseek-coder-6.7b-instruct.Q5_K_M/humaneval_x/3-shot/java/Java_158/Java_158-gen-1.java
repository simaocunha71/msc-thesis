        String maxWord = "";
        int maxUnique = 0;

        for (String word : words) {
            Set<Character> uniqueChars = new HashSet<>();
            for (char c : word.toCharArray()) {
                uniqueChars.add(c);
            }
            if (uniqueChars.size() > maxUnique ||
                (uniqueChars.size() == maxUnique && word.compareTo(maxWord) < 0)) {
                maxUnique = uniqueChars.size();
                maxWord = word;
            }
        }

        return maxWord;
     }
}

