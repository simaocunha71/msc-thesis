        List<Integer> result = new ArrayList<>();
        int count_even = 0;
        int count_odd = 0;

        for (int i = 1; i < n; i++) {
            String num_string = Integer.toString(i);
            if (num_string.equals(new StringBuilder(num_string).reverse().toString())) {
                if (i % 2 == 0) count_even += 1;
                else count_odd += 1;
            }
        }
        result.add(count_even);
        result.add(count_odd);
        return result;
    }
}

