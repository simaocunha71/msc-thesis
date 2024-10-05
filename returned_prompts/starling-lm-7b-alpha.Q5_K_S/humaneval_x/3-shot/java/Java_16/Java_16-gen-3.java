        Set<Character> characters = new HashSet<>();
        for (char c : string.toLowerCase().toCharArray()) {
            characters.add(c);
        }
        return characters.size();
    }
}

