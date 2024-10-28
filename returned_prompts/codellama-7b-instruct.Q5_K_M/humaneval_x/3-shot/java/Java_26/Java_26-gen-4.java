        return numbers.stream().filter(n -> Collections.frequency(numbers, n) == 1).collect(Collectors.toList());
    }
}

