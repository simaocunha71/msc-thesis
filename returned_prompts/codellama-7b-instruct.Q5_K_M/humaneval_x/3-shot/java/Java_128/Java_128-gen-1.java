        if (arr.isEmpty()) return Optional.empty();

        int product = 1;
        int sum = 0;
        for (int e : arr) {
            product *= e < 0 ? -1 : 1;
            sum += Math.abs(e);
        }
        return Optional.of(product * sum);
    }
}

