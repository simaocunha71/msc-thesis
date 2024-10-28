        if (arr.isEmpty()) return Collections.emptyList();

        int smallest_even_value = Integer.MAX_VALUE;
        int smallest_even_index = -1;

        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0 && arr.get(i) < smallest_even_value) {
                smallest_even_value = arr.get(i);
                smallest_even_index = i;
            }
        }

        if (smallest_even_index == -1) return Collections.emptyList();
        arr.remove(smallest_even_index);
        return Arrays.asList(smallest_even_value, smallest_even_index);
    }
}

