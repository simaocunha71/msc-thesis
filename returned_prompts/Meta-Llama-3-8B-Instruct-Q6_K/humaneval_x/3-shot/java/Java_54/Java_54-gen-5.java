        if (s0.length() != s1.length()) {
            return false;
        }

        Map<Character, Integer> s0_count = new HashMap<>();
        Map<Character, Integer> s1_count = new HashMap<>();

        for (char c : s0.toCharArray()) {
            s0_count.put(c, s0_count.getOrDefault(c, 0) + 1);
        }

        for (char c : s1.toCharArray()) {
            s1_count.put(c, s1_count.getOrDefault(c, 0) + 1);
        }

        return s0_count.equals(s1_count);
    }
}

