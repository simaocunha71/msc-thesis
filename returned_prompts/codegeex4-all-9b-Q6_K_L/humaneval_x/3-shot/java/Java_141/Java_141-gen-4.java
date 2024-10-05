        String[] parts = file_name.split("\\.");
        if (parts.length != 2 || parts[1].length() > 3) {
            return "No";
        }

        String[] valid_extensions = {"txt", "exe", "dll"};
        if (Arrays.stream(valid_extensions).noneMatch(parts[1]::equals)) {
            return "No";
        }

        for (char c : parts[0].toCharArray()) {
            if (c < 'a' || c > 'z' && (c < 'A' || c > 'Z')) {
                return "No";
            }
        }

        return "Yes";
    }
}

