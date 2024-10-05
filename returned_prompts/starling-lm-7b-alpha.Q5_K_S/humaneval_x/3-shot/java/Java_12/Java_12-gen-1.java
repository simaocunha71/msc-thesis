        Optional<String> result = Optional.empty();
        int max_length = 0;

        for (String s : strings) {
            if (s.length() > max_length) {
                max_length = s.length();
                result = Optional.of(s);
            }
        }
        return result;
    }
}

