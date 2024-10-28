        String[] extensions = {"txt", "exe", "dll"};
        String[] parts = file_name.split("\\.");

        if (parts.length != 2) return "No";
        if (!Character.isLetter(parts[0].charAt(0))) return "No";
        if (parts[0].matches("\\d{4,}")) return "No";
        if (!Arrays.asList(extensions).contains(parts[1])) return "No";
        return "Yes";
    }
}

