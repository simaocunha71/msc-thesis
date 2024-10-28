        if (arr.size() == 0) return Optional.empty();

        int total_product = 1;
        int total_sum = 0;

        for (int n : arr) {
            if (n == 0) continue;
            total_product *= n > 0 ? 1 : -1;
            total_sum += Math.abs(n);
        }
        return Optional.of(total_sum * total_product);
    }
}

