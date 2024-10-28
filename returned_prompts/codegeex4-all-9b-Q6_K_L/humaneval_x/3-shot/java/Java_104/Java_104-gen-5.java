        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < x.size(); i++) {
            int current_number = x.get(i);
            boolean has_even_digit = false;
            while (current_number != 0) {
                if (current_number % 2 == 0) {
                    has_even_digit = true;
                    break;
                }
                current_number /= 10;
            }
            if (!has_even_digit) {
                result.add(x.get(i));
            }
        }
        Collections.sort(result);
        return result;
    }
}

