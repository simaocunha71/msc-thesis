        for (int i = arr.size() - 1; i >= 0; i--) {
            if (arr.get(i) <= arr.get(i - 1)) {
                continue;
            }
            for (int j = i - 1; j >= 0; j--) {
                if (arr.get(i) > arr.get(j)) {
                    return j;
                }
            }
        }
        return -1;
    }
}
