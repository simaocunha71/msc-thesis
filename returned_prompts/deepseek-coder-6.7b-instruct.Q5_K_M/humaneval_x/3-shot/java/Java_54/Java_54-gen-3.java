        int[] count = new int[256];
        for (char c : s0.toCharArray()) count[c]++;
        for (char c : s1.toCharArray()) count[c]--;
        for (int i : count) if (i != 0) return false;
        return true;
     }
}

