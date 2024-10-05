        List<Integer> result = new ArrayList<>();
        if (arr.size() == 0) {
            return result;
        }
        int smallest_even = arr.get(0);
        int smallest_index = 0;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0 && arr.get(i) < smallest_even) {
                smallest_even = arr.get(i);
                smallest_index = i;
            }
        }
        result.add(smallest_even);
        result.add(smallest_index);
        return result;
    }
}

