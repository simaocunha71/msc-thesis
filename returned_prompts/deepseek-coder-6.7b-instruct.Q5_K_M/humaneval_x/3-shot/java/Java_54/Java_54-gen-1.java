        Map<Character, Integer> map = new HashMap<>();
        for (char c : s0.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        for (char c : s1.toCharArray()) {
            if (map.containsKey(c)) {
                int count = map.get(c);
                if (count == 1) {
                    map.remove(c);
                } else {
                    map.put(c, count - 1);
                }
            } else {
                return false;
            }
        }
        return map.isEmpty();
    }
}

