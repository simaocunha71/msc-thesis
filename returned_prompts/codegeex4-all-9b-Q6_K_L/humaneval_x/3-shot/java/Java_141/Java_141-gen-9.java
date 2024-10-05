        String[] parts = file_name.split("\\.");
        if (parts.length != 2) {
            return "No";
        }

        String name = parts[0];
        String extension = parts[1];
        if (name.length() > 3 || name.length() == 0) {
            return "No";
        }

        for (char c : name.toCharArray()) {
            if (c < 'a' || c > 'z' && c < 'A' || c > 'Z') {
                return "No";
            }
        }

        if (!extension.equals("txt") && !extension.equals("exe") && !extension.equals("dll")) {
            return "No";
        }
        return "Yes";

    }
}

