        String[] extensions = {"txt", "exe", "dll"};
        String[] parts = file_name.split("\\.");

        if (parts.length != 2) {
            return "No";
        }

        String prefix = parts[0];
        String suffix = parts[1];

        if (!prefix.matches("[a-zA-Z].*") || prefix.matches(".*\\d{4,}.*") || suffix.length() > 3 || !Arrays.asList(extensions).contains(suffix)) {
            return "No";
        }

        return "Yes";
    }
}

