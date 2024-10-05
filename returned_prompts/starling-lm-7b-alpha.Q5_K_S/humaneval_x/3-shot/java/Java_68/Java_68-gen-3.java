        List<Integer> result = new ArrayList<>();
        int smallest_even_value = Integer.MAX_VALUE;
        int smallest_even_index = -1;

        for (int i = 0; i < arr.size(); i++) {
            int value = arr.get(i);
            if (value % 2 == 0 && value < smallest_even_value) {
                smallest_even_value = value;
                smallest_even_index = i;
            }
        }
        if (smallest_even_value != Integer.MAX_VALUE) {
            result.add(smallest_even_value);
            result.add(smallest_even_index);
        }
        return result;
    }
}

