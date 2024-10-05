        if (arr.size() == 0) return Optional.empty();

        int result = 1;
        for (int num : arr) {
            int sign = num > 0 ? 1 : num < 0 ? -1 : 0;
            result *= sign;
        }
        return Optional.of(result);
    }
}

