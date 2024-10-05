        int even_count = 0;
        int odd_count = 0;
        for (int i = 0; i < String.valueOf(Math.abs(num)).length(); i++) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                even_count += 1;
            } else {
                odd_count += 1;
            }
            num /= 10;
        }
        List<Integer> result = new ArrayList<>();
        result.add(even_count);
        result.add(odd_count);
        return result;
    }
}

