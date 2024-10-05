        if (s0.length() != s1.length()) return false;
        Map<Character, Integer> map0 = new HashMap<>();
        Map<Character, Integer> map1 = new HashMap<>();

        for (char c : s0.toCharArray()) {
            map0.put(c, map0.getOrDefault(c, 0) + 1);
        }
        for (char c : s1.toCharArray()) {
            map1.put(c, map1.getOrDefault(c, 0) + 1);
        }

        return map0.equals(map1);
    }
}

