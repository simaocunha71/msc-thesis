        String longest = "";

        for (String string : strings) {
            if (string.length() > longest.length()) {
                longest = string;
            }
        }
        return Optional.ofNullable(longest);
    }
}

