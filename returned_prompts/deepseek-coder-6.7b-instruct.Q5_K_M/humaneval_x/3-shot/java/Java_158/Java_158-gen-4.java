        String maxWord = "";
        for  (String word : words) {
            Set<Character> uniqueChars = new HashSet<>();
            for  (char c : word.toCharArray()) {
                uniqueChars.add(c);
            }
            if  (uniqueChars.size() > maxWord.length()) {
                maxWord = word;
            } else if  (uniqueChars.size() == maxWord.length() && word.compareTo(maxWord) < 0) {
                maxWord = word;
            }
        }
        return maxWord;
     }
}

