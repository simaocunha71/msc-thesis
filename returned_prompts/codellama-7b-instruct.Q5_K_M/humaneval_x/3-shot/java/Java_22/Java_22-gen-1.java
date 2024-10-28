        return values.stream()
                .filter(v -> v instanceof Integer)
                .map(v -> (Integer) v)
                .collect(Collectors.toList());
    }
}

