        int max_index = 0;
        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i) > arr.get(max_index)) max_index = i;
        }
        for (int i = 0; i < arr.size(); i++) {
            if (i == max_index) continue;
            if (arr.get(i) > arr.get((i + 1) % arr.size())) return false;
        }
        return true;
    }
}

