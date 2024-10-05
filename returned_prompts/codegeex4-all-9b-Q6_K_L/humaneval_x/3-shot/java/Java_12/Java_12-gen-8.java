        if (strings.isEmpty()) {
            return Optional.empty();
        }

        String longest_string = strings.get(0);

        for (String s : strings) {
            if (s.length() > longest_string.length()) {
                longest_string = s;
            }
        }

        return Optional.of(longest_string);
    }
}

