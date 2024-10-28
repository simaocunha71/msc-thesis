        List<Integer> result = new ArrayList<>();
        int smallest = Integer.MAX_VALUE;
        int index = -1;
        int i = 0;

        for (int node : arr) {
            if (node % 2 == 0 && node < smallest) {
                smallest = node;
                index = i;
            }
            i += 1;
        }
        if (index == -1) return result;
        result.add(smallest);
        result.add(index);
        return result;
    }
}

