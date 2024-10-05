        List<Integer> result = new ArrayList<>();
        if (arr.isEmpty()) return result;
        int min_even_value = Integer.MAX_VALUE;
        int min_even_index = Integer.MAX_VALUE;

        for (int i = 0; i < arr.size(); i++) {
            int value = arr.get(i);
            if (value % 2 == 0 && value < min_even_value) {
                min_even_value = value;
                min_even_index = i;
            }
        }

        if (min_even_value == Integer.MAX_VALUE) return result;

        result.add(min_even_value);
        result.add(min_even_index);
        return result;
    }
}

