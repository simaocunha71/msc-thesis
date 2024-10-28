        List<Integer> result = new ArrayList<>();
        if (arr.isEmpty()) return result;

        int smallest_value = Integer.MAX_VALUE;
        int smallest_index = -1;
        for (int i = 0; i < arr.size(); i++) {
            int num = arr.get(i);
            if (num % 2 == 0 && num < smallest_value) {
                smallest_value = num;
                smallest_index = i;
            }
        }

        if (smallest_index == -1) return result;

        result.add(smallest_value);
        result.add(smallest_index);
        return result;

    }
}

