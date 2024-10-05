        int max_index = -1;
        for (int i = 0; i < arr.size(); i++) {
            if (i > 0 && arr.get(i) <= arr.get(i - 1)) {
                return max_index;
            }
            max_index = i;
        }
        return max_index;
    }
}

