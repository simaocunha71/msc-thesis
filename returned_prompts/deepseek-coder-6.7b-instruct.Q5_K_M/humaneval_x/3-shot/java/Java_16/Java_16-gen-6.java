        Set<Character> distinctCharacters = new HashSet<>();

        for(char c : string.toCharArray()) {
            distinctCharacters.add(Character.toLowerCase(c));
        }

        return distinctCharacters.size();
     }
}

