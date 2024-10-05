        if (arr.isEmpty()) return Optional.empty();
        int product = 1;
        for (int i : arr) {
            product *= i;
        }
        return Optional.of(product);
    }
}

