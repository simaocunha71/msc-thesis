        return values.stream()
                .filter(val -> val instanceof Integer)
                .map(val -> (Integer) val)
                .collect(Collectors.toList());
    }
}

