        List<Integer> result = new ArrayList<>();
        int min_value = Integer.MAX_VALUE;
        int min_value_index = -1;

        for (int i = 0; i < arr.size(); i++) {
            int value = arr.get(i);
            if (value % 2 == 0 && value < min_value) {
                min_value = value;
                min_value_index = i;
            }
        }
        if (min_value_index != -1) {
            result.add(min_value);
            result.add(min_value_index);
        }
        return result;
    }
}



```