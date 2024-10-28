        if (arr.size() == 0) return true;
        int max = arr.get(0);
        int index = 0;

        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i) > max) {
                max = arr.get(i);
                index = i;
            }
        }

        for (int i = index; i < arr.size(); i++) {
            arr.set(i, arr.get(i + 1));
        }
        arr.set(0, max);

        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) > arr.get((i + 1) % arr.size())) return false;
        }
        return true;
    }
}

