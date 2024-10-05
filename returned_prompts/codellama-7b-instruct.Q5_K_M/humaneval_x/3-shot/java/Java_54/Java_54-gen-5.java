        if (s0.length() != s1.length()) return false;

        // map each character to its count in s0
        HashMap<Character, Integer> char_counts = new HashMap<>();
        for (char c : s0.toCharArray()) {
            int count = 0;
            if (char_counts.containsKey(c)) count = char_counts.get(c);
            char_counts.put(c, count + 1);
        }

        // check if each character in s1 is also in s0 and its count is the same
        for (char c : s1.toCharArray()) {
            if (!char_counts.containsKey(c) || char_counts.get(c) == 0) return false;
            char_counts.put(c, char_counts.get(c) - 1);
        }
        return true;
    }
}

