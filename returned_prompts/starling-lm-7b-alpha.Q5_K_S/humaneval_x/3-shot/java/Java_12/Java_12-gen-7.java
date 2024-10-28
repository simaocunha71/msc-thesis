        if (strings.isEmpty()) return Optional.empty();
        int max_length = 0;
        String max_string = "";
        for (String s : strings) {
            if (s.length() > max_length) {
                max_length = s.length();
                max_string = s;
            }
        }
        return Optional.of(max_string);
    }
}

