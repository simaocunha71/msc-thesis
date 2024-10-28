        if (arr.isEmpty()) return Optional.empty();

        int product = 1;
        int sum = 0;
        for (int num : arr) {
            int sign = num >= 0 ? 1 : -1;
            product *= sign;
            sum += Math.abs(num) * sign;
        }
        return Optional.of(sum * product);
    }
}

