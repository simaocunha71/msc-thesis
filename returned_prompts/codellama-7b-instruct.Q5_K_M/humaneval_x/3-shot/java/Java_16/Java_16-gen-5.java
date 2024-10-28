        Set<Character> char_set = new HashSet<>();
        char[] chars = string.toLowerCase().toCharArray();
        for (char c : chars) {
            char_set.add(c);
        }
        return char_set.size();
    }
}

