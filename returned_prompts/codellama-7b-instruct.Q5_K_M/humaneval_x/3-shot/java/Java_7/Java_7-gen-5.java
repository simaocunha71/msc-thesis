        return strings.stream()
                .filter(s -> s.contains(substring))
                .collect(Collectors.toList());
    }
}

