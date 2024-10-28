        List<Integer> result = new ArrayList<>();
        int even = 0;
        int odd = 0;

        while (num > 0) {
            if (num % 10 % 2 == 0) {
                even += 1;
            } else {
                odd += 1;
            }
            num /= 10;
        }
        result.add(even);
        result.add(odd);
        return result;
    }
}

