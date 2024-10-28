        List<Integer> result = new ArrayList<>();
        int smallest_even = Integer.MAX_VALUE;
        int smallest_even_index = -1;

        for (int i = 0; i < arr.size(); i++) {
            int val = arr.get(i);
            if (val % 2 == 0 && val < smallest_even) {
                smallest_even = val;
                smallest_even_index = i;
            }
        }

        if (smallest_even_index != -1) {
            result.add(smallest_even);
            result.add(smallest_even_index);
        }

        return result;

    }
}

