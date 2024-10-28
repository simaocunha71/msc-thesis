        int sum = 0;
        int product = 1;

        for (int number : numbers) {
            sum += number;
            product *= number;
        }

        return List.of(sum, product);
    }
}

