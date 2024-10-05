        return numbers.stream().filter(i -> Collections.frequency(numbers, i) == 1).collect(Collectors.toList());
    }
}

