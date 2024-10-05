        List<Integer> result = new ArrayList<>();
        int current_number = n;

        while (current_number != 1) {
            if (current_number % 2 == 1) {
                result.add(current_number);
                current_number = current_number * 3 + 1;
            } else {
                current_number = current_number / 2;
            }
        }
        result.add(current_number);
        Collections.sort(result);
        return result;
    }
}

