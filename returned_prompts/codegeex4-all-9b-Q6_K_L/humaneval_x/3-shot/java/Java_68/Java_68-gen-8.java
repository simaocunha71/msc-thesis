        int smallest_even_value = Integer.MAX_VALUE;
        int smallest_even_index = Integer.MAX_VALUE;
        for (int i = 0; i < arr.size(); i++) {
            int current_value = arr.get(i);
            if (current_value % 2 == 0 && current_value < smallest_even_value) {
                smallest_even_value = current_value;
                smallest_even_index = i;
            }
        }

        if (smallest_even_index == Integer.MAX_VALUE) {
            return new ArrayList<>();
        } else {
            return Arrays.asList(smallest_even_value, smallest_even_index);
        }
    }
}

