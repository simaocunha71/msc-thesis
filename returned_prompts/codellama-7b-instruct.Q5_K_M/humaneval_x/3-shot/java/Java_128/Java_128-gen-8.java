        if (arr.size() == 0) return Optional.empty();
        int product = 1;
        int sum = 0;
        for (int i : arr) {
            product *= i > 0 ? 1 : i < 0 ? -1 : 0;
            sum += Math.abs(i);
        }
        return Optional.of(product * sum);
    }
}

