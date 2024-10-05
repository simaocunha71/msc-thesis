        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < k; i++) {
            int max_index = i;
            for (int j = i + 1; j < arr.size(); j++) {
                if (arr.get(j) > arr.get(max_index)) {
                    max_index = j;
                }
            }
            result.add(arr.get(max_index));
            arr.set(max_index, Integer.MIN_VALUE);
        }
        return result;
    }
}

