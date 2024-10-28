        List<Integer> result = new ArrayList<>();
        int current = n;
        while (current != 1) {
            if (current % 2 == 0) {
                current /= 2;
            } else {
                current = 3 * current + 1;
            }
            if (current % 2 != 0) {
                result.add(current);
            }
        }
        if (current % 2 != 0) {
            result.add(1);
        }
        Collections.sort(result);
        return result;
    }
}

