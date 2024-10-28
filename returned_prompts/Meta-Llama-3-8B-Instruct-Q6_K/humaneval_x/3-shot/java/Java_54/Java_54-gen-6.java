        Map<Character, Integer> count0 = new HashMap<>();
        Map<Character, Integer> count1 = new HashMap<>();

        for (char c : s0.toCharArray()) {
            count0.put(c, count0.getOrDefault(c, 0) + 1);
        }
        for (char c : s1.toCharArray()) {
            count1.put(c, count1.getOrDefault(c, 0) + 1);
        }
        return count0.equals(count1);
    }
}

