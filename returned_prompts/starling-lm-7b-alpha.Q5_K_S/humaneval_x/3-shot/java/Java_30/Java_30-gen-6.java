        return l.stream()
            .filter(number -> number > 0)
            .collect(Collectors.toList());
    }
}

