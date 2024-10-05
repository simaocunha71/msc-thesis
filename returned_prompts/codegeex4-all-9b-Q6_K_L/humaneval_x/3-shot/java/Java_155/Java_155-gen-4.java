        int even = 0, odd = 0;
        String num_str = Integer.toString(Math.abs(num));
        for (char c : num_str.toCharArray()) {
            int digit = Character.getNumericValue(c);
            if (digit % 2 == 0) even += 1;
            else odd += 1;
        }
        return Arrays.asList(even, odd);
    }
}

