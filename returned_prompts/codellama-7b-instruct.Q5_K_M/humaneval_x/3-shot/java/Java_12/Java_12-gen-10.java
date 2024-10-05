        if (strings.isEmpty()) {
            return Optional.empty();
        }

        String longest_string = strings.get(0);
        int longest_length = longest_string.length();

        for (String string : strings) {
            int length = string.length();
            if (length > longest_length) {
                longest_string = string;
                longest_length = length;
            }
        }
        return Optional.of(longest_string);
    }
}

