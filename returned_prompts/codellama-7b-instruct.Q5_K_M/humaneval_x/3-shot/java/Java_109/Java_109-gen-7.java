        if (arr.size() == 0) return true;
        int i = 0;
        while (i < arr.size()) {
            int j = i + 1;
            while (j < arr.size()) {
                if (arr.get(i) > arr.get(j)) {
                    // swap i, j
                    int temp = arr.get(i);
                    arr.set(i, arr.get(j));
                    arr.set(j, temp);
                }
                j += 1;
            }
            i += 1;
        }
        for (i = 1; i < arr.size(); i++) {
            if (arr.get(i) < arr.get(i - 1)) return false;
        }
        return true;
    }
}

