        String[] parts = file_name.split("\\.");
        if (parts.length != 2 || parts[0].length() == 0) {
            return "No";
        }

        if (parts[0].length() > 3 || !parts[0].matches("[a-zA-Z][a-zA-Z0-9]*")) {
            return "No";
        }

        return Arrays.asList("txt", "exe", "dll").contains(parts[1]) ? "Yes" : "No";
    }
}

