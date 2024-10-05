        List<Integer> result = new ArrayList<>();
        int current_value = n;

        while (current_value != 1) {
            if (current_value % 2 == 0) {
                current_value /= 2;
            } else {
                current_value = 3 * current_value + 1;
            }
            result.add(current_value);
        }

        return result;
    }
}

