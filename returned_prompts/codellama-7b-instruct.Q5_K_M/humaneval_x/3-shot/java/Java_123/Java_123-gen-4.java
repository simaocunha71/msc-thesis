        List<Integer> result = new ArrayList<>();
        List<Integer> sequence = new ArrayList<>();
        while (n != 1) {
            if (n % 2 == 0) {
                n /= 2;
            } else {
                n = 3 * n + 1;
            }
            sequence.add(n);
        }
        sequence.add(1);
        for (Integer num : sequence) {
            if (num % 2 != 0) {
                result.add(num);
            }
        }
        return result;
    }
}

