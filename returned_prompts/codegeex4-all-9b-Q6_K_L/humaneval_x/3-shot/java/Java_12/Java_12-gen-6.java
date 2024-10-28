        Optional<String> longest_string = Optional.empty();
        int max_length = 0;

        for (String s : strings) {
            if (s.length() > max_length) {
                longest_string = Optional.of(s);
                max_length = s.length();
            }
        }
        return longest_string;
    }
}

