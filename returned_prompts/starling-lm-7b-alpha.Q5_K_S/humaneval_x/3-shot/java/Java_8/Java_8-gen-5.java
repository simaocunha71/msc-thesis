        int sum = 0;
        long product = 1;
        for (Integer number : numbers) {
            sum += number;
            product *= number;
        }
        return List.of(sum, (int) product);
    }
}

