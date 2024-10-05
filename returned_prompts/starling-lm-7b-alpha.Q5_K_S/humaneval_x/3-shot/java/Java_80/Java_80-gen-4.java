        if (s.length() < 3) return false;
        Map<Character, Integer> count = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            if (count.containsKey(s.charAt(i))) {
                count.put(s.charAt(i), count.get(s.charAt(i)) + 1);
            } else {
                count.put(s.charAt(i), 1);
            }
        }
        for (int i = 0; i + 2 < s.length(); i++) {
            if (count.get(s.charAt(i)) == 0) {
                return false;
            } else {
                count.put(s.charAt(i), count.get(s.charAt(i)) - 1);
            }
            if (count.get(s.charAt(i + 1)) == 0) {
                return false;
            } else {
                count.put(s.charAt(i + 1), count.get(s.charAt(i + 1)) - 1);
            }
            if (count.get(s.charAt(i + 2)) == 0) {
                return false;
            } else {
                count.put(s.charAt(i + 2), count.get(s.charAt(i + 2)) - 1);
            }
        }
        return true;
    }
}

