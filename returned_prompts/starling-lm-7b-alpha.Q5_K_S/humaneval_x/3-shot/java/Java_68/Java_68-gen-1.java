        int smallest_even = Integer.MAX_VALUE;
        int index = -1;

        for (int i = 0; i < arr.size(); i++) {
            int value = arr.get(i);
            if (value % 2 == 0 && value < smallest_even) {
                smallest_even = value;
                index = i;
            }
        }
        return new ArrayList<>(Collections.singletonList(smallest_even));
    }
}

