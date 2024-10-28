        Set<Character> distinct_characters = new HashSet<>();
        for  (char c  : string.toCharArray()) {
            distinct_characters.add(Character.toLowerCase(c));
        }
        return distinct_characters.size();
     }
}

