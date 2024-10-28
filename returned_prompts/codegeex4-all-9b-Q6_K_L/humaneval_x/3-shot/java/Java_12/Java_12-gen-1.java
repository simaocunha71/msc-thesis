        Optional<String> result = Optional.empty();

        for (String s : strings) {
            if (result.isEmpty() || s.length() > result.get().length()) {
                result = Optional.of(s);
            }
        }
        return result;

    }
}

