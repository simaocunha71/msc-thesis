        String[] extensions = {"txt", "exe", "dll"};
        String[] parts = file_name.split("\\.");
        if (parts.length != 2) return "No";
        String name = parts[0];
        String extension = parts[1];
        if (!name.matches("^[a-zA-Z][a-zA-Z0-9]*$") || name.matches("[0-9]+") || name.length() > 3) return "No";
        if (!Arrays.asList(extensions).contains(extension)) return "No";
        return "Yes";
    }
}

