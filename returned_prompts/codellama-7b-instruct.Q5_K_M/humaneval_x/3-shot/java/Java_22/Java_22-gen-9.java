        return values.stream()
                .filter(value -> value instanceof Integer)
                .map(value -> (Integer) value)
                .collect(Collectors.toList());
    }
}

