        Map<Character, Integer> charCounts0 = getCharCounts(s0);
        Map<Character, Integer> charCounts1 = getCharCounts(s1);

        return charCounts0.equals(charCounts1);
    }

    private Map<Character, Integer> getCharCounts(String s) {
        Map<Character, Integer> charCounts = new HashMap<>();
        for (char c : s.toCharArray()) {
            charCounts.put(c, charCounts.getOrDefault(c, 0) + 1);
        }
        return charCounts;
    }
}

