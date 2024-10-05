        if (strings.size() == 0) return Optional.empty();
        Collections.sort(strings, (a, b) -> b.length() - a.length());
        return Optional.of(strings.get(0));
    }
}

