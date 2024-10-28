        int max = -1, freq = 0;
        for (int i : lst) {
            if (i > max && freq < i) {
                max = i;
                freq = 1;
            } else if (i == max) {
                freq += 1;
            }
        }

        if (freq >= max) return -1;
        return max;
    }
}

