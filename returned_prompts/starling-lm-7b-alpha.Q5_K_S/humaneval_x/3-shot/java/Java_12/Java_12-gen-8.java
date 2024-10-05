        if (strings.size() == 0) return Optional.empty();
        String longest_string = strings.get(0);
        for (String s : strings) {
            if (longest_string.length() < s.length()) {
                longest_string = s;
            }
        }
        return Optional.of(longest_string);
    }
}

