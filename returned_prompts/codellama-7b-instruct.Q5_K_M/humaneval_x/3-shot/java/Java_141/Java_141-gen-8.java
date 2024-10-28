        if (file_name.length() > 3) return "No";
        if (!file_name.contains(".")) return "No";
        if (file_name.substring(0, file_name.indexOf(".")).length() == 0) return "No";
        if (!(file_name.substring(file_name.indexOf(".") + 1).equals("txt")
                || file_name.substring(file_name.indexOf(".") + 1).equals("exe")
                || file_name.substring(file_name.indexOf(".") + 1).equals("dll"))) {
            return "No";
        }
        return "Yes";

    }
}

