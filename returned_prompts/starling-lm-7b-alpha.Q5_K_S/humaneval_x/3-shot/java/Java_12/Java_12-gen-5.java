        if (strings.size() == 0) {
            return Optional.empty();
        }

        String longest = strings.get(0);
        for (String s : strings) {
            if (s.length() > longest.length()) {
                longest = s;
            }
        }
        return Optional.of(longest);
    }
}

