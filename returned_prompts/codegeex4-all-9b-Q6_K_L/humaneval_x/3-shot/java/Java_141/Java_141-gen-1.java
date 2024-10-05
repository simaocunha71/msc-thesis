        int dot_index = file_name.indexOf('.');
        if (dot_index == -1) return "No";
        if (file_name.length() > 3 && Character.isDigit(file_name.charAt(0))) return "No";
        String extension = file_name.substring(dot_index + 1);
        if (extension.equals("txt") || extension.equals("exe") || extension.equals("dll")) return "Yes";
        return "No";
    }
}

