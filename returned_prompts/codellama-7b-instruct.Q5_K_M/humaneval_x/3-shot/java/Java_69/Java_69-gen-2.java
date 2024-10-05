        int max_freq = 0;
        int max_val = -1;

        for (int i : lst) {
            int freq = 0;
            for (int j : lst) {
                if (i == j) freq++;
            }
            if (freq > max_freq) {
                max_freq = freq;
                max_val = i;
            }
        }

        if (max_freq < 1) return -1;
        return max_val;
    }
}

