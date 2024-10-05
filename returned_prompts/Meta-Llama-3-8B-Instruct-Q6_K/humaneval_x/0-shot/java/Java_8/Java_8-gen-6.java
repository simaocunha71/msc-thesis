        if (numbers.isEmpty()) {
            return Arrays.asList(0, 1);
        }
        int sum = 0;
        int product = 1;
        for (int num : numbers) {
            sum += num;
            product *= num;
        }
        return Arrays.asList(sum, product);
    }
}