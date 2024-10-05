        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < x.size(); i++) {
            boolean has_even_digit = false;
            int current_number = x.get(i);

            while (current_number > 0) {
                int current_digit = current_number % 10;
                if (current_digit % 2 == 0) {
                    has_even_digit = true;
                    break;
                }
                current_number = current_number / 10;
            }

            if (!has_even_digit) {
                result.add(x.get(i));
            }
        }
        Collections.sort(result);
        return result;
    }
}

