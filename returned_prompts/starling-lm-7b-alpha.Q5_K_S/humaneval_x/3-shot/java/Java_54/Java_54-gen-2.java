        if (s0.length() != s1.length()) return false;
        Map<Character, Integer> counts = new HashMap<>();
        for (char c : s0.toCharArray()) {
            counts.put(c, counts.getOrDefault(c, 0) + 1);
        }
        for (char c : s1.toCharArray()) {
            if (counts.getOrDefault(c, 0) == 0) return false;
            counts.put(c, counts.get(c) - 1);
        }
        return true;
    }
}

