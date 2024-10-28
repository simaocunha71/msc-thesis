        int sum = 0;
        long product = 1;

        for (int number : numbers) {
            sum += number;
            product *= number;
        }

        return List.of(sum, (int) product);
    }
}

