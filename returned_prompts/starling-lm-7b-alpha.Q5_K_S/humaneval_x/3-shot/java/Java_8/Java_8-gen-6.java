        int sum = 0;
        long product = 1;
        for (Integer n : numbers) {
            sum += n;
            product *= n;
        }
        return List.of(sum, (int) product);
    }
}

