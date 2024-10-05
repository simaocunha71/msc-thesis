        String number_string = Integer.toString(num);
        int even_count = 0;
        int odd_count = 0;

        for (char c : number_string.toCharArray()) {
            int digit = Character.getNumericValue(c);
            if (digit % 2 == 0) even_count += 1;
            else odd_count += 1;
        }
        return Arrays.asList(even_count, odd_count);
    }
}

