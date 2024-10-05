        List<Integer> result = new ArrayList<>();
        int even_count = 0;
        int odd_count = 0;
        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                even_count += 1;
            } else {
                odd_count += 1;
            }
            num /= 10;
        }
        result.add(even_count);
        result.add(odd_count);
        return result;
    }
}

