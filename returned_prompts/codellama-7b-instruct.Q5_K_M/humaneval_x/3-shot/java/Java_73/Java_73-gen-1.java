        int[] counts = new int[10000];
        int min_count = 0;
        int max_val = 0;
        for (int val : arr) {
            min_count += counts[val];
            counts[val]++;
            max_val = Math.max(max_val, val);
        }
        int min_diff = 0;
        for (int i = 0; i < max_val; i++) {
            min_diff = Math.min(min_diff, counts[i] % 2);
        }
        return min_diff + min_count;
    }
}

