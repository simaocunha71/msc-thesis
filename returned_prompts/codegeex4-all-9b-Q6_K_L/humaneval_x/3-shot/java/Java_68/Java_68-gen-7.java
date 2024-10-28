        List<Integer> result = new ArrayList<>();
        int min_index = -1;
        int min_value = Integer.MAX_VALUE;

        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0 && arr.get(i) <= min_value) {
                min_value = arr.get(i);
                min_index = i;
            }
        }

        if (min_index == -1) return result;
        result.add(min_value);
        result.add(min_index);
        return result;
    }
}

