        int max = -1;
        int freq = -1;

        for (int i : lst) {
            if (i > max) {
                max = i;
                freq = 1;
            } else if (i == max) {
                freq += 1;
            }
        }

        for (int i = 1; i <= max; i++) {
            if (freq >= i) return i;
        }
        return -1;
    }
}

