        String[] extensions = {"txt", "exe", "dll"};
        String[] parts = file_name.split("\\.");
        if (parts.length != 2) return "No";
        if (!Character.isLetter(parts[0].charAt(0))) return "No";
        String extension = parts[1].trim().toLowerCase();
        if (!Arrays.asList(extensions).contains(extension)) return "No";
        int digitCount = 0;
        for (char c : parts[0].toCharArray()) {
            if (Character.isDigit(c)) digitCount++;
        }
        return digitCount <= 3 ? "Yes" : "No";
    }
}

