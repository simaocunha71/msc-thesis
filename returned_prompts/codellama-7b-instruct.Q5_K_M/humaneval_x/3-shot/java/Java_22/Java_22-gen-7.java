        return values.stream()
                .filter(Object::isInteger)
                .map(Object::intValue)
                .collect(Collectors.toList());
    }
}

