        if (s0.length() != s1.length()) return false;
        Map<Character, Integer> freq_map = new HashMap<>();
        for (char c : s0.toCharArray()) {
            freq_map.merge(c, 1, Integer::sum);
        }
        for (char c : s1.toCharArray()) {
            if (!freq_map.containsKey(c) || freq_map.get(c) == 0) return false;
            freq_map.merge(c, -1, Integer::sum);
        }
        return true;
    }
}

