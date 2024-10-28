        if (strings.isEmpty()) return Optional.empty();
        String longest_string = strings.get(0);
        for (String string : strings) {
            if (string.length() > longest_string.length()) {
                longest_string = string;
            }
        }
        return Optional.of(longest_string);
    }
}

