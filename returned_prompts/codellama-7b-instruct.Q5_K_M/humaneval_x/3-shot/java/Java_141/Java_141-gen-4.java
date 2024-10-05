        int digit_count = 0;
        for (char c : file_name.toCharArray()) {
            if (c >= '0' && c <= '9') digit_count += 1;
            if (digit_count > 3) return "No";
        }

        if (file_name.contains("..") || file_name.contains("..") || file_name.contains("..")) return "No";
        if (!file_name.contains(".")) return "No";
        if (file_name.substring(0, file_name.indexOf('.')).length() == 0) return "No";
        if (file_name.substring(file_name.indexOf('.') + 1).equals("txt") ||
            file_name.substring(file_name.indexOf('.') + 1).equals("exe") ||
            file_name.substring(file_name.indexOf('.') + 1).equals("dll")) return "Yes";
        return "No";
    }
}

