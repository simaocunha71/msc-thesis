        if (arr.isEmpty()) return new ArrayList<>();

        int smallest_even = 0, smallest_index = 0;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0 && arr.get(i) < smallest_even) {
                smallest_even = arr.get(i);
                smallest_index = i;
            }
        }

        if (smallest_even == 0) return new ArrayList<>();

        List<Integer> result = new ArrayList<>();
        result.add(smallest_even);
        result.add(smallest_index);
        return result;
    }
}

