        int even_count = 0;
        int odd_count = 0;
        String str = String.valueOf(num);

        for (char c : str.toCharArray()) {
            int digit = Character.getNumericValue(c);

            if (digit % 2 == 0) {
                even_count += 1;
            } else {
                odd_count += 1;
            }
        }
        return Arrays.asList(even_count, odd_count);
    }
}

