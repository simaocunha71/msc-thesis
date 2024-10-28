        List<Integer> result = new ArrayList<>();
        int smallest_value = Integer.MAX_VALUE;
        int smallest_index = -1;

        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0 && arr.get(i) < smallest_value) {
                smallest_value = arr.get(i);
                smallest_index = i;
            }
        }

        if (smallest_value != Integer.MAX_VALUE) {
            result.add(smallest_value);
            result.add(smallest_index);
        } else {
            result = new ArrayList<>();
        }

        return result;

    }
}

