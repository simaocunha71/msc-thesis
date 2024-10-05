        int min_val = Integer.MAX_VALUE;
        int min_idx = -1;
        int smallest_idx = -1;
        int smallest_val = Integer.MAX_VALUE;

        for (int i = 0; i < arr.size(); i++) {
            int val = arr.get(i);
            if ((val & 1) == 0 && val < min_val) {
                min_val = val;
                min_idx = i;
            }
            if (val < smallest_val && (val & 1) == 0) {
                smallest_val = val;
                smallest_idx = i;
            }
        }

        if (smallest_idx == -1) {
            smallest_idx = min_idx;
        }

        List<Integer> res = new ArrayList<>();
        res.add(arr.get(smallest_idx));
        res.add(smallest_idx);

        arr.remove(smallest_idx);

        return res;
    }
}
