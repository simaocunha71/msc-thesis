        String[] extensions = {"txt", "exe", "dll"};
        String[] parts = file_name.split("\\.");
        if (parts.length != 2) return "No";
        String prefix = parts[0];
        String suffix = parts[1];
        if (!prefix.matches("^[a-zA-Z][a-zA-Z0-9]*$")) return "No";
        if (prefix.matches(".*\\d.*") && prefix.replaceAll("\\d", "").length() > 3) return "No";
        if (!Arrays.asList(extensions).contains(suffix)) return "No";
        return "Yes";
    }
}

