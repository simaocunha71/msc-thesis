        List<Integer> result = new ArrayList<>();

        result.add(0);
        result.add(1);
        result.add(2);
        result.add(3);

        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                result.add((int) ((double) result.get(i) / 2.0));
            } else {
                int current_value = (int) result.get(i - 1) + (int) result.get(i - 2) + (int) result.get(i + 1);
                result.add(current_value);
            }
        }
        return result;
    }
}

