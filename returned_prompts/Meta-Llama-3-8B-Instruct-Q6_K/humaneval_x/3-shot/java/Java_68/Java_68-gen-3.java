        List<Integer> result = new ArrayList<>();
        int min_even_value = Integer.MAX_VALUE;
        int min_even_index = -1;

        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0 && arr.get(i) < min_even_value) {
                min_even_value = arr.get(i);
                min_even_index = i;
            }
        }

        if (min_even_index != -1) {
            result.add(min_even_value);
            result.add(min_even_index);
        } else {
            result.add([]);
        }
        return result;
    }
}

