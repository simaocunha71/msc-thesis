        if (strings.isEmpty()) return Optional.empty();

        Comparator<String> length_comparator = Comparator.comparingInt(String::length);
        Comparator<String> natural_order = Comparator.naturalOrder();
        Comparator<String> comparator = length_comparator.thenComparing(natural_order);

        return strings.stream().min(comparator);
    }
}

