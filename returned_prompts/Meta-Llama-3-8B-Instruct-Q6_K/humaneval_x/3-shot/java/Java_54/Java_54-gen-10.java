        if (s0.length() != s1.length()) return false;

        Map<Character, Integer> s0_map = new HashMap<>();
        Map<Character, Integer> s1_map = new HashMap<>();

        for (char c : s0.toCharArray()) {
            s0_map.put(c, s0_map.getOrDefault(c, 0) + 1);
        }
        for (char c : s1.toCharArray()) {
            s1_map.put(c, s1_map.getOrDefault(c, 0) + 1);
        }

        return s0_map.equals(s1_map);
    }
}

