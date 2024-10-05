        if (arr.isEmpty()) return true;
        if (arr.size() == 1) return true;

        int max = arr.get(0);
        int index = 0;
        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i) > max) {
                max = arr.get(i);
                index = i;
            }
        }
        if (index == 0) return false;

        Collections.swap(arr, 0, index);
        Collections.reverse(arr.subList(1, arr.size()));
        return true;
    }
}

