        if (strings.isEmpty()) {
            return Optional.empty();
        }

        String result = strings.get(0);
        for (String string : strings) {
            if (string.length() > result.length()) {
                result = string;
            }
        }
        return Optional.of(result);
    }
}

