        List<Integer> result = new ArrayList<>();
        if (arr.isEmpty()) return result;

        int smallest_even_value = 0;
        int smallest_even_index = 0;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0) {
                if (smallest_even_value == 0) {
                    smallest_even_value = arr.get(i);
                    smallest_even_index = i;
                } else if (arr.get(i) < smallest_even_value) {
                    smallest_even_value = arr.get(i);
                    smallest_even_index = i;
                }
            }
        }

        result.add(smallest_even_value);
        result.add(smallest_even_index);
        return result;

    }
}

