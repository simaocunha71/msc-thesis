        List<Integer> result = new ArrayList<>();
        int smallest = Integer.MAX_VALUE;
        int smallest_index = -1;

        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0 && arr.get(i) < smallest) {
                smallest = arr.get(i);
                smallest_index = i;
            }
        }

        if (smallest_index != -1) {
            result.add(smallest);
            result.add(smallest_index);
            arr.set(smallest_index, 0);
        } else {
            result.add(0);
            result.add(0);
        }
        return result;
    }
}

