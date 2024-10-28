        if (s0.length() != s1.length()) return false;
        Map<Character, Integer> map = new HashMap<>();
        for (char c : s0.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        for (char c : s1.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) - 1);
        }
        for (int count : map.values()) {
            if (count != 0) return false;
        }
        return true;
    }
}

