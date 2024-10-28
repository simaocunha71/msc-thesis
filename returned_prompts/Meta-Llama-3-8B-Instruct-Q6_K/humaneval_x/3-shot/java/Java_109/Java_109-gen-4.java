        int min = Integer.MAX_VALUE;
        for (int i : arr) {
            if (i < min) {
                min = i;
            }
        }
        int last = arr.get(arr.size() - 1);
        for (int i = 0; i < arr.size() - 1; i++) {
            if (arr.get(i) > last) {
                return false;
            }
        }
        return true;
    }
}

