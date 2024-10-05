        List<Integer> result = new ArrayList<>();

        for (int num : x) {
            boolean has_even_digit = false;
            int current_num = num;
            while (current_num > 0) {
                int digit = current_num % 10;
                if (digit % 2 == 0) {
                    has_even_digit = true;
                    break;
                }
                current_num /= 10;
            }

            if (!has_even_digit) {
                result.add(num);
            }
        }

        Collections.sort(result);
        return result;

    }
}

