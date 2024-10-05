        if (strings.isEmpty()) return Optional.empty();

        String longest_string = strings.get(0);
        for (String current_string : strings) {
            if (current_string.length() > longest_string.length()) {
                longest_string = current_string;
            }
        }
        return Optional.of(longest_string);
    }
}

