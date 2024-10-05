        Map<Character, Integer> char_count = new HashMap<>();
        for (char c : s0.toCharArray()) {
            char_count.put(c, char_count.getOrDefault(c, 0) + 1);
        }
        for (char c : s1.toCharArray()) {
            char_count.put(c, char_count.get(c) - 1);
        }
        for (int count : char_count.values()) {
            if (count != 0) return false;
        }
        return true;
    }
}


```