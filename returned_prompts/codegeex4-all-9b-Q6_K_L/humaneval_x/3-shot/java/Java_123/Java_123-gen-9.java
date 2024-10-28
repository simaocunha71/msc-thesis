        List<Integer> result = new ArrayList<>();
        int current_number = n;
        while (current_number != 1) {
            if (current_number % 2 == 0) {
                current_number /= 2;
            } else {
                result.add(current_number);
                current_number = 3 * current_number + 1;
            }
        }
        result.add(1);
        Collections.sort(result);
        return result;
    }
}

