        int max_index = 0;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) > arr.get(max_index)) {
                max_index = i;
            }
        }
        int max = arr.get(max_index);
        arr.remove(max_index);
        arr.add(0, max);
        return arr.equals(Arrays.asList(1, 2, 3, 4, 5));
    }
}


