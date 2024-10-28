        if (arr.size() == 0) return Optional.empty();

        int product = 1;
        int sum = 0;

        for (int number : arr) {
            product *= Math.signum(number);
            sum += Math.abs(number);
        }
        return Optional.of(product * sum);
    }
}

