        int[] count = new int[26];
        for (char c : s0.toCharArray()) count[c - 'a']++;
        for (char c : s1.toCharArray()) count[c - 'a']--;
        for (int i : count) if (i != 0) return false;
        return true;
    }
}

