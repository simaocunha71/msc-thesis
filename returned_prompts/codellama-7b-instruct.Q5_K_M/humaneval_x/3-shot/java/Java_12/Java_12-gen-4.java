        if (strings.isEmpty()) return Optional.empty();
        int max_length = 0;
        String longest_string = "";

        for (String string : strings) {
            if (string.length() > max_length) {
                max_length = string.length();
                longest_string = string;
            }
        }
        return Optional.of(longest_string);
    }
}

