        int smallest_even = Integer.MAX_VALUE;
        int smallest_even_index = -1;

        for (int i = 0; i < arr.size(); i++) {
            int node = arr.get(i);
            if (node % 2 == 0 && node < smallest_even) {
                smallest_even = node;
                smallest_even_index = i;
            }
        }

        if (smallest_even == Integer.MAX_VALUE) {
            return new ArrayList<>();
        } else {
            return Arrays.asList(smallest_even, smallest_even_index);
        }
    }
}

