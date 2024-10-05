        Set<Character> unique_chars = new HashSet<>();

        for (char c : string.toCharArray()) {
            unique_chars.add(c);
        }

        return unique_chars.size();
    }
}

