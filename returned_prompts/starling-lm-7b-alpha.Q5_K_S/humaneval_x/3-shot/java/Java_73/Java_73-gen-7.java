        Collections.sort(arr);
        int half = (arr.size() + 1) / 2;
        int change_count = 0;
        for (int i = 0; i < half; i++) {
            if (arr.get(i) != arr.get(arr.size() - 1 - i)) {
                change_count += 1;
            }
        }
        return change_count;
    }
}

