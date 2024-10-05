        if (arr.isEmpty()) return Optional.empty();

        int result = 1;
        for (int a : arr) result *= a >= 0 ? 1 : -1;
        return Optional.of(result * arr.stream().mapToInt(i -> Math.abs(i)).sum());
    }
}

