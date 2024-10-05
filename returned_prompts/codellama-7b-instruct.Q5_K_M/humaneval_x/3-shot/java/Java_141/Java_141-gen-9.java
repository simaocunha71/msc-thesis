        int count = 0;
        String[] parts = file_name.split("\\.");
        if (parts.length != 2) {
            return "No";
        }
        for (char c : parts[0].toCharArray()) {
            if (!Character.isLetter(c)) {
                if (count > 3) {
                    return "No";
                }
                count++;
            }
        }
        if (count > 3) {
            return "No";
        }

        for (String ext : parts[1].split("\\.")) {
            if (ext.equals("exe") || ext.equals("dll") || ext.equals("txt")) {
                return "Yes";
            }
        }
        return "No";
    }
}

