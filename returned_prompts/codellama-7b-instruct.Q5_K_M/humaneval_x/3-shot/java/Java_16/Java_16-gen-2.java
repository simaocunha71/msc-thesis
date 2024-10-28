        Set<Character> seen_chars = new HashSet<>();
        for (char c : string.toLowerCase().toCharArray()) {
            seen_chars.add(c);
        }
        return seen_chars.size();
    }
}

