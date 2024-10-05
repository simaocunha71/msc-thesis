        if (strings.size() == 0) return Optional.empty();

        Optional<String> result = Optional.of(strings.get(0));
        for (String string : strings) {
            if (result.get().length() < string.length()) result = Optional.of(string);
        }
        return result;
    }
}

