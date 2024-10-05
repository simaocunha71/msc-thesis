        if (arr.isEmpty()) {
            return Optional.empty();
        } else {
            int prod = 1;
            int sum = 0;
            for (int a : arr) {
                prod *= (a < 0) ? -1 : 1;
                sum += Math.abs(a);
            }
            return Optional.of(prod * sum);
        }
    }
}

