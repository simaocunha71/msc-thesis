        return strings.stream()
                .max(Comparator.comparingInt(String::length))
                .map(Optional::of);
    }
}

