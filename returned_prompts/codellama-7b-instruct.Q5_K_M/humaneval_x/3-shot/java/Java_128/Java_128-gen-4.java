        if (arr.isEmpty()) return Optional.empty();
        int product = 1;
        int sum = 0;
        for (Integer num : arr) {
            int sign = (num > 0) ? 1 : (num < 0) ? -1 : 0;
            sum += Math.abs(num);
            product *= sign;
        }
        return Optional.of(product * sum);
    }
}

