        if (strings.isEmpty()) {
            return Optional.empty();
        } else {
            return Optional.of Collections.max(strings, (a, b) -> a.length() - b.length());
        }
    }
}

