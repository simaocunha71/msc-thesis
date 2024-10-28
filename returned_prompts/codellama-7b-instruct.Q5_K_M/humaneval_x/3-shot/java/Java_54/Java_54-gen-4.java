        if (s0.length() != s1.length()) return false;
        boolean[] char_seen = new boolean[26];
        for (char c : s0.toCharArray()) char_seen[c - 'a'] = true;
        for (char c : s1.toCharArray()) if (!char_seen[c - 'a']) return false;
        return true;
    }
}

