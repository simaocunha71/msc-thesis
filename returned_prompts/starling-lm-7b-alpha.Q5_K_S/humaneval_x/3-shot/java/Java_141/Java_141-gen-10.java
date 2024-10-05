        if (file_name.length() == 0) return "No";
        if (file_name.length() > 3) return "No";
        if (file_name.length() == 1 && Character.isDigit(file_name.charAt(0))) return "No";
        if (file_name.length() == 2 && Character.isDigit(file_name.charAt(1))) return "No";
        if (file_name.length() > 2 && Character.isDigit(file_name.charAt(2))) return "No";
        int dot_index = file_name.indexOf('.');
        if (dot_index == -1) return "No";
        if (dot_index == 0) return "No";
        String prefix = file_name.substring(0, dot_index);
        String suffix = file_name.substring(dot_index + 1);

        if (prefix.isEmpty()) return "No";
        if (!Character.isAlphabetic(prefix.charAt(0))) return "No";
        if (suffix.isEmpty()) return "No";
        if (!suffix.equals("txt") && !suffix.equals("exe") && !suffix.equals("dll")) return "No";

        return "Yes";
    }
}

