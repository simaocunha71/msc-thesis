        int max_freq = 0;
        int max_val = -1;
        Set<Integer> seen = new HashSet<>();

        for (int i : lst) {
            if (seen.contains(i)) continue;
            seen.add(i);

            int freq = 1;
            for (int j : lst) {
                if (i == j) freq++;
            }
            if (freq >= i && freq > max_freq) {
                max_freq = freq;
                max_val = i;
            }
        }
        return max_val;
    }
}

