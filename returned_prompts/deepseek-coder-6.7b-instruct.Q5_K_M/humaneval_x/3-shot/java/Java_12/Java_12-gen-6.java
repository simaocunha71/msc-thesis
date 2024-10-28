        if (strings.isEmpty()) return Optional.empty();

        return strings.stream().max(Comparator.comparing(String::length));
     }
}

