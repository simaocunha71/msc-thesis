        String[] tokens = file_name.split("\\.");
        if (tokens.length != 2) return "No";
        if (tokens[0].matches(".*\\d.*")) return "No";
        if (tokens[0].length() > 3) return "No";
        if (tokens[0].matches(".*[a-zA-Z].*")) {
            if (tokens[1].matches(".*[txt|exe|dll].*")) return "Yes";
        }
        return "No";
    }
}

