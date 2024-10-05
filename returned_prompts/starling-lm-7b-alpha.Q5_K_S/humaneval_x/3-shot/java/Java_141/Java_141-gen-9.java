        if (file_name.length() < 2 || file_name.length() > 8) return "No";
        if (!Character.isLetter(file_name.charAt(0))) return "No";
        if (file_name.indexOf('.') == -1) return "No";
        if (file_name.indexOf('.') != file_name.lastIndexOf('.')) return "No";
        String[] valid_extensions = new String[]{"txt", "exe", "dll"};
        int file_type_length = file_name.length() - file_name.indexOf('.') - 1;
        if (Arrays.asList(valid_extensions).contains(file_name.substring(file_name.length() - file_type_length)) &&
                file_name.substring(1, file_name.indexOf('.')).matches("\\d{0,3}")) {
            return "Yes";
        } else {
            return "No";
        }
    }
}

