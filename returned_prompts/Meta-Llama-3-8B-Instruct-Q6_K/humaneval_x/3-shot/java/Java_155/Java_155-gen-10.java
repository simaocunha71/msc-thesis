        List<Integer> result = new ArrayList<>();
        int even = 0, odd = 0;

        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                even++;
            } else {
                odd++;
            }
            num /= 10;
        }
        result.add(even);
        result.add(odd);
        return result;
    }
}

