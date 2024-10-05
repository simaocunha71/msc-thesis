        if (s0.length() != s1.length()) return false;
        Map<Character, Integer> char_map = new HashMap<>();
        for (char c : s0.toCharArray()) {
            char_map.put(c, char_map.getOrDefault(c, 0) + 1);
        }
        for (char c : s1.toCharArray()) {
            char_map.put(c, char_map.get(c) - 1);
            if (char_map.get(c) < 0) return false;
        }
        return true;
    }
}

