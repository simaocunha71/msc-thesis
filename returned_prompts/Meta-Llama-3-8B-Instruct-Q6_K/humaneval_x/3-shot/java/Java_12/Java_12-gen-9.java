        if (strings.isEmpty()) {
            return Optional.empty();
        }
        String longest = strings.get(0);
        for (String str : strings) {
            if (str.length() > longest.length()) {
                longest = str;
            }
        }
        return Optional.of(longest);
    }
}

