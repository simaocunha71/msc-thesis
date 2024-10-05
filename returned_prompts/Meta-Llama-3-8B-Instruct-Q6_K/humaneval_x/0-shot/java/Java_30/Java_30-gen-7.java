    return l.stream()
            .filter(num -> num > 0)
            .collect(Collectors.toList());
}  // This will return a list of all the positive numbers in the input list. It uses Java 8 Stream API to achieve this.

