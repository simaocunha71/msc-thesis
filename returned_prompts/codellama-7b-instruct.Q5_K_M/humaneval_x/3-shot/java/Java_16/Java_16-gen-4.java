        Set<Character> char_set = new HashSet<>();

        for (char c : string.toCharArray()) {
            char_set.add(Character.toLowerCase(c));
        }
        return char_set.size();
    }
}

