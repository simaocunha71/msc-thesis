        if (s0.length() != s1.length()) return false;

        Map<Character, Integer> count = new HashMap<>();
        for (char c : s0.toCharArray()) {
            count.put(c, count.getOrDefault(c, 0) + 1);
        }
        for (char c : s1.toCharArray()) {
            if (count.get(c) == null || count.get(c) == 0) return false;
            count.put(c, count.get(c) - 1);
        }
        return true;
    }
}

