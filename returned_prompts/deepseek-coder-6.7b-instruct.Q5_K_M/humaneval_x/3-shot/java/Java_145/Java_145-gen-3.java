        return nums.stream()
            .sorted(Comparator.comparingInt(i -> Integer.toString(i).chars().map(c -> Math.abs(c - '0')).sum()))
            .collect(Collectors.toList());
    }
}

