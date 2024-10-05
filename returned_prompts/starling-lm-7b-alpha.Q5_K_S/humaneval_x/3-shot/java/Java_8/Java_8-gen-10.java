        int sum = 0;
        int product = 1;

        for (int n : numbers) {
            sum += n;
            product *= n;
        }
        return List.of(sum, product);
    }
}

