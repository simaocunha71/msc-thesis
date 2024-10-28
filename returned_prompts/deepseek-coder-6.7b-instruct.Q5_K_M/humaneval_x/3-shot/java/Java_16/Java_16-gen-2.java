        Set<Character> distinct_chars = new HashSet<>();
        for  (char c : string.toCharArray()) {
            distinct_chars.add(Character.toLowerCase(c));
        }
        return distinct_chars.size();
    }
}

