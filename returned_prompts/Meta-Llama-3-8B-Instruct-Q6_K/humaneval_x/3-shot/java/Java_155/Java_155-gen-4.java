        List<Integer> result = new ArrayList<>();
        int even_count = 0, odd_count = 0;
        while (num != 0) {
            int digit = num % 10;
            if (digit % 2 == 0) even_count++;
            else odd_count++;
            num /= 10;
        }
        result.add(even_count);
        result.add(odd_count);
        return result;
    }
}

