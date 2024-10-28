        String maxWord = "";
        int maxCount = 0;

        for(String word : words){
            Set<Character> uniqueChars = new HashSet<>();
            for(char c : word.toCharArray()){
                uniqueChars.add(c);
            }
            if(uniqueChars.size() > maxCount){
                maxCount = uniqueChars.size();
                maxWord = word;
            } else if(uniqueChars.size() == maxCount){
                if(word.compareTo(maxWord) < 0){
                    maxWord = word;
                }
            }
        }

        return maxWord;
    }
}

