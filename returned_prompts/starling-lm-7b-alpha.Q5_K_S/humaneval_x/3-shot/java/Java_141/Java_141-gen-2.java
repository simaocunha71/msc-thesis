        String[] valid_extensions = new String[] { "txt", "exe", "dll" };
        String[] invalid_chars = new String[] { "", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" };

        String[] parts = file_name.split("\\.");
        if (parts.length != 2) return "No";

        String part_before_dot = parts[0];
        String part_after_dot = parts[1];
        if (part_before_dot.isEmpty()) return "No";
        if (part_after_dot.isEmpty()) return "No";

        for (String part : parts) {
            if (part.matches(".*[0-9].*")) {
                if (invalid_chars.length == part.length()) return "No";
            } else {
                if (!part.matches("^[a-zA-Z]")) return "No";
            }
        }

        if (!Arrays.asList(valid_extensions).contains(part_after_dot)) {
            return "No";
        }

        return "Yes";
    }
}

