        if (s0.length() != s1.length()) return false;
        Map<Character, Integer> char_map = new HashMap<>();
        for (char c : s0.toCharArray()) {
            char_map.merge(c, 1, Integer::sum);
        }
        for (char c : s1.toCharArray()) {
            if (char_map.getOrDefault(c, 0) == 0) return false;
            char_map.merge(c, -1, Integer::sum);
        }
        return true;
    }
}

