        List<Optional<Integer>> result = new ArrayList<>();
        int largest = -1;
        int smallest = -1;
        for (Integer i : lst) {
            if (i < 0) {
                if (i > largest) {
                    largest = i;
                }
            } else {
                if (smallest == -1) {
                    smallest = i;
                } else if (i < smallest) {
                    smallest = i;
                }
            }
        }
        result.add(Optional.ofNullable(largest));
        result.add(Optional.ofNullable(smallest));
        return result;
    }
}

