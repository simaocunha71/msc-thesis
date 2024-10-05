        if (s0.length() != s1.length()) return false;
        int[] char_count = new int[26];
        for (char c : s0.toCharArray()) {
            char_count[c - 'a'] += 1;
        }
        for (char c : s1.toCharArray()) {
            char_count[c - 'a'] -= 1;
            if (char_count[c - 'a'] < 0) return false;
        }
        return true;
    }
}

