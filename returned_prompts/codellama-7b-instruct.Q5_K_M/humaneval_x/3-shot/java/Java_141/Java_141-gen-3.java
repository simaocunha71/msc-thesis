        if (file_name.length() > 3) return "No";
        int dot_pos = file_name.indexOf(".");
        if (dot_pos == -1) return "No";
        if (file_name.charAt(0) < 'a' || file_name.charAt(0) > 'z') return "No";
        String ext = file_name.substring(dot_pos + 1);
        if (ext.equals("txt") || ext.equals("exe") || ext.equals("dll")) {
            return "Yes";
        } else {
            return "No";
        }
    }
}

