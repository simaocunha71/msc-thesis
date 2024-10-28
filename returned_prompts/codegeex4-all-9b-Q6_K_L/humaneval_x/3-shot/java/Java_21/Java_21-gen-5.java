        double min = Collections.min(numbers);
        double max = Collections.max(numbers);
        return numbers.stream().map(n -> (n - min) / (max - min)).collect(Collectors.toList());
    }
}

