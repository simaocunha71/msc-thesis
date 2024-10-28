        List<Integer> result = new ArrayList<>();
        if (arr.isEmpty()) return result;

        int smallest_even = Integer.MAX_VALUE;
        int smallest_index = -1;

        for (int i = 0; i < arr.size(); i++) {
            int value = arr.get(i);
            if (value % 2 == 0 && value < smallest_even) {
                smallest_even = value;
                smallest_index = i;
            }
        }

        if (smallest_index >= 0) {
            result.add(smallest_even);
            result.add(smallest_index);
        }

        return result;
    }
}

