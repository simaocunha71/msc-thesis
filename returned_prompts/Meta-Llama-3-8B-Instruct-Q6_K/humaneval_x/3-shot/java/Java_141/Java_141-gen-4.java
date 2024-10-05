        String[] extensions = {"txt", "exe", "dll"};
        if (!file_name.matches("^[a-zA-Z]+\\.[a-zA-Z0-9]{1,3}$")) {
            return "No";
        }
        String[] parts = file_name.split("\\.");
        if (!Arrays.asList(extensions).contains(parts[1])) {
            return "No";
        }
        return "Yes";
    }
}

