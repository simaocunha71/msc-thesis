        String[] extensions = {"txt", "exe", "dll"};
        String[] parts = file_name.split("\\.");

        if (parts.length != 2) {
            return "No";
        }

        String before_dot = parts[0];
        String after_dot = parts[1].toLowerCase();

        if (!before_dot.matches("[a-zA-Z][a-zA-Z0-9]*") || before_dot.matches("[0-9]{4,}")) {
            return "No";
        }

        if (!Arrays.asList(extensions).contains(after_dot)) {
            return "No";
        }

        return "Yes";
    }
}