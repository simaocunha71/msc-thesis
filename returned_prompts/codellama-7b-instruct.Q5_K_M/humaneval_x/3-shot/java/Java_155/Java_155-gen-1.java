        List<Integer> result = new ArrayList<>();
        int even_count = 0;
        int odd_count = 0;

        while (num > 0) {
            int last_digit = num % 10;
            num /= 10;
            if (last_digit % 2 == 0) {
                even_count += 1;
            } else {
                odd_count += 1;
            }
        }
        result.add(even_count);
        result.add(odd_count);
        return result;

    }
}

