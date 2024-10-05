        List<Integer> result = new ArrayList<>();
        if (arr.size() == 0) return result;

        int min_even = Integer.MAX_VALUE;
        int min_even_index = -1;

        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0) {
                if (arr.get(i) < min_even) {
                    min_even = arr.get(i);
                    min_even_index = i;
                } else if (arr.get(i) == min_even && i < min_even_index) {
                    min_even_index = i;
                }
            }
        }
        if (min_even_index != -1) {
            result.add(min_even_index);
            result.add(min_even);
        }
        return result;
    }
}

