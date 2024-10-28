        return strings.stream()
            .filter(s -> s.startsWith(prefix))
            .collect(Collectors.toList());
    }
}

