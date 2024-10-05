        if (arr.isEmpty()) return Optional.empty();

        int result = 1;
        for (int i : arr) {
            if (i < 0) {
                result *= -1;
            } else if (i == 0) {
                return Optional.of(0);
            }
        }
        return Optional.of(result);
    }
}

