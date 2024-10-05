        List<Integer> result = new ArrayList<>();
        int smallest_even = Integer.MAX_VALUE;
        int smallest_index = -1;

        for (int i = 0; i < arr.size(); i++) {
            int node_value = arr.get(i);
            if (node_value % 2 == 0 && node_value < smallest_even) {
                smallest_even = node_value;
                smallest_index = i;
            }
        }

        if (smallest_even == Integer.MAX_VALUE) return result;
        result.add(smallest_even);
        result.add(smallest_index);
        return result;
    }
}

