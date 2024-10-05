        String maxWord = "";
        int maxCount = 0;

        for (String word : words) {
            Set<Character> uniqueChars = new HashSet<>();
            for (char c : word.toCharArray()) {
                uniqueChars.add(c);
            }
            if (uniqueChars.size() > maxCount || (uniqueChars.size() == maxCount && word.compareTo(maxWord) < 0)) {
                maxCount = uniqueChars.size();
                maxWord = word;
            }
        }

        return maxWord;
    }
}

