        int sum = 0;
        int product = 1;

        if (numbers.isEmpty()) {
            return List.of(sum, product);
        }

        for (int number : numbers) {
            sum += number;
            product *= number;
        }

        return List.of(sum, product);
    }
}

