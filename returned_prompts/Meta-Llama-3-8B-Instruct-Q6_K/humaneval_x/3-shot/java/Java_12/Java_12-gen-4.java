        if (strings.isEmpty()) {
            return Optional.empty();
        }
        Optional<String> result = Optional.of(strings.get(0));
        for (String s : strings) {
            if (s.length() > result.get().length()) {
                result = Optional.of(s);
            }
        }
        return result;
    }
}

