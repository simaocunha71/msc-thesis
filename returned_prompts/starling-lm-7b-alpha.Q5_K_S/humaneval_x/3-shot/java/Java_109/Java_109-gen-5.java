        int min_index = Collections.minElement(arr);
        int min_index_original = arr.indexOf(min_index);

        int i = 0;
        while (i < arr.size()) {
            if (arr.get(i) == min_index) {
                if (i == min_index_original) {
                    i += 1;
                    continue;
                } else {
                    return false;
                }
            }
            i += 1;
        }
        return true;
    }
}

