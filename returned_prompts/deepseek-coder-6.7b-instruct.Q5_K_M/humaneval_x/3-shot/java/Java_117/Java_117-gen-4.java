        List<String> words = Arrays.asList(s.split(" "));
        List<String> selectedWords = new ArrayList<>();
        String consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";

        for(String word : words){
            int count = 0;
            for(char letter : word.toCharArray()){
                if(consonants.indexOf(letter) != -1){
                    count++;
                }
            }
            if(count == n){
                selectedWords.add(word);
            }
        }
        return selectedWords;
     }
}

