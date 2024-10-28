        List<Integer> result = new ArrayList<>();
        int max_index = 0;
        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i) > arr.get(max_index)) max_index = i;
        }
        int max = arr.get(max_index);
        arr.set(max_index, -100000);
        if (k == 0) return result;
        result.add(max);
        return maximum(arr, k - 1);
    }
}

