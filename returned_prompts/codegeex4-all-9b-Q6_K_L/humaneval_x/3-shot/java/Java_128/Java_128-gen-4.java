        if (arr.isEmpty()) return Optional.empty();
        int product = 1;
        int sum = 0;

        for (int num : arr) {
            if (num < 0) product *= -1;
            sum += Math.abs(num);
        }
        return Optional.of(product * sum);
    }
}

