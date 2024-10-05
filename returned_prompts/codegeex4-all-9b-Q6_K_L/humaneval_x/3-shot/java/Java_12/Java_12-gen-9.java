        if (strings.isEmpty()) return Optional.empty();

        String longest = strings.get(0);
        for (String string : strings) {
            if (string.length() > longest.length()) longest = string;
        }
        return Optional.of(longest);
    }
}

