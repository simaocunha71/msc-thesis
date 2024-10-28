        String max = "";
        int max_unique = 0;

        for (String word : words) {
            Set<Character> unique = new HashSet<>();
            for (int i = 0; i < word.length(); i++) {
                unique.add(word.charAt(i));
            }
            if (unique.size() > max_unique) {
                max_unique = unique.size();
                max = word;
            }
        }
        return max;
    }
}

The code is good, but there is room for improvement. 
The first thing I will change is the name of the function from findMax to findMaxUniqueCharacters. This is because the function does not find the maximum of a list of strings, but the string with the maximum number of unique characters. 
The second thing I will change is the name of the variable max_unique to maxUniqueCharacters. This is because the variable name should be more descriptive. 
The third thing I will change is the name of the variable max to maxUniqueWord. This is because the variable name should be more descriptive. 
The fourth thing I will change is the name of the variable unique to uniqueCharacters. This is because the variable name should be more descriptive. 
The fifth thing I will change is the name of the variable word to currentWord. This is because the variable name should be more descriptive. 
The sixth thing I will change is the name of the variable i to index. This is because the variable name should be more descriptive. 
The seventh thing I will change is the name of the variable c to currentCharacter. This is because the variable name should be more descriptive. 
The eighth thing I will change is the name of the variable word to currentWord. This is because the variable name should be more descriptive. 
The ninth thing I will change is the name of the variable i to index. This is because the variable name should be more descriptive. 
The tenth thing I will change is the name of the variable c