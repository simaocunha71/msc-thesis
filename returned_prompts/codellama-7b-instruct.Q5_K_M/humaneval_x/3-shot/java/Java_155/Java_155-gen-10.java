        List<Integer> result = new ArrayList<>();
        int count_even = 0;
        int count_odd = 0;

        while (num != 0) {
            if (num % 10 % 2 == 0) {
                count_even += 1;
            } else {
                count_odd += 1;
            }
            num /= 10;
        }
        result.add(count_even);
        result.add(count_odd);
        return result;
    }
}

