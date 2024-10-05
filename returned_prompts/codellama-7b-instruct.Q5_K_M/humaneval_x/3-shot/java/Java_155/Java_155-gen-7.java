        List<Integer> result = new ArrayList<>();
        int count_even = 0;
        int count_odd = 0;

        while (num > 0) {
            int last_digit = num % 10;
            if (last_digit % 2 == 0) count_even++;
            else count_odd++;

            num /= 10;
        }
        result.add(count_even);
        result.add(count_odd);
        return result;
    }
}

