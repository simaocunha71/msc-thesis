        if (strings.isEmpty()) return Optional.empty();
        String longest = strings.get(0);
        for (String s : strings) {
            if (longest.length() < s.length()) {
                longest = s;
            }
        }
        return Optional.of(longest);
    }
}

