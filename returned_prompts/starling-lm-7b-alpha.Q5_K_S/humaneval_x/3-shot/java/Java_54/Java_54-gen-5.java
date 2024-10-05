        if (s0.length() != s1.length()) return false;

        Map<Character, Integer> counter = new HashMap<>();
        for (char c : s0.toCharArray()) {
            counter.put(c, counter.getOrDefault(c, 0) + 1);
        }

        for (char c : s1.toCharArray()) {
            if (counter.get(c) == null || counter.get(c) == 0) return false;
            counter.put(c, counter.get(c) - 1);
        }
        return true;
    }
}

