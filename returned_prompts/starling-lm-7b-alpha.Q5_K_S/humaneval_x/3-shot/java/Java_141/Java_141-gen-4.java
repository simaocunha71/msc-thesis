        if (file_name.contains("..") || file_name.contains(".")) return "No";
        String[] parts = file_name.split("\\.");
        if (parts.length != 2) return "No";
        if (parts[0].length() == 0 || !Character.isLetter(parts[0].charAt(0))) return "No";
        if (!parts[1].equals("txt") && !parts[1].equals("exe") && !parts[1].equals("dll")) return "No";
        return "Yes";
    }
}

