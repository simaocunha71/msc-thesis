        int[] counts = new int[256];
        for (char c : s0.toCharArray()) counts[c]++;
        for (char c : s1.toCharArray()) counts[c]--;
        for (int count : counts) if (count != 0) return false;
        return true;
     }
}

