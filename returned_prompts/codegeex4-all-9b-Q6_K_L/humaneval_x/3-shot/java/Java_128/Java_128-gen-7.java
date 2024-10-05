        if (arr.size() == 0) return Optional.empty();

        int product = 1;
        int sum = 0;
        for (int num : arr) {
            product *= Math.signum(num);
            sum += Math.abs(num);
        }

        return Optional.of(product * sum);
    }
}

