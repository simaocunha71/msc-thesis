        if (arr.isEmpty()) return Optional.empty();

        int product = 1;
        int sum = 0;

        for (int element : arr) {
            product *= (element > 0) ? 1 : (element < 0) ? -1 : 0;
            sum += Math.abs(element);
        }
        return Optional.of(product * sum);
    }
}

