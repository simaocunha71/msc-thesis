        List<Integer> result = new ArrayList<>();
        int current_number = 2;

        while (result.size() < n) {
            boolean is_prime = true;
            for (int i = 2; i < current_number; i++) {
                if (current_number % i == 0) {
                    is_prime = false;
                    break;
                }
            }

            if (is_prime) result.add(current_number);
            current_number += 1;
        }
        return result;
    }
}

