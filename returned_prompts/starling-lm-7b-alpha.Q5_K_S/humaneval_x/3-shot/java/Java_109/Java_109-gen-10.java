        int max_index = 0;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) > arr.get(max_index)) {
                max_index = i;
            }
        }
        int max_value = arr.get(max_index);
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) == max_value) {
                arr.set(i, -1);
            }
        }
        Collections.sort(arr);
        return arr.size() == 0 || (arr.size() == 1 && arr.get(0) == -1);
    }
}

