        List<Integer> result = new ArrayList<>();
        int smallest_even_index = -1;
        int smallest_even_value = Integer.MAX_VALUE;

        for (int i = 0; i < arr.size(); i++) {
            int value = arr.get(i);
            if (value % 2 == 0 && value < smallest_even_value) {
                smallest_even_index = i;
                smallest_even_value = value;
            }
        }

        if (smallest_even_index != -1) {
            result.add(smallest_even_value);
            result.add(smallest_even_index);
        } else {
            result.add(new ArrayList<>());
        }

        return result;
    }
}

