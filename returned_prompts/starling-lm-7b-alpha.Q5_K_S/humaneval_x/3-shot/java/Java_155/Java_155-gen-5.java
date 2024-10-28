        int even = 0;
        int odd = 0;

        while (num != 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                even += 1;
            } else {
                odd += 1;
            }
            num /= 10;
        }

        List<Integer> result = new ArrayList<>();
        result.add(even);
        result.add(odd);
        return result;
    }
}

