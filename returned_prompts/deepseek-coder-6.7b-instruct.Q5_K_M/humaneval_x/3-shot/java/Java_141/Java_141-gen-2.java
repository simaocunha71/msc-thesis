        String[] parts = file_name.split("\\.");
        if (parts.length != 2) return "No";
        String name = parts[0];
        String extension = parts[1];
        if (name.length() == 0 || !Character.isLetter(name.charAt(0))) return "No";
        if (extension.length() > 3 || !(extension.equals("txt") || extension.equals("exe") || extension.equals("dll"))) return "No";
        int digitCount = 0;
        for (char c : name.toCharArray()) {
            if (Character.isDigit(c)) digitCount += 1;
        }
        if (digitCount > 3) return "No";
        return "Yes";
    }
}

