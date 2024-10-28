        if (file_name.length() > 3) return "No";
        if (file_name.indexOf(".") == -1) return "No";
        if (file_name.indexOf(".") == 0) return "No";
        if (!Character.isLetter(file_name.charAt(0))) return "No";
        if (file_name.substring(file_name.indexOf(".") + 1).equals("exe") || file_name.substring(file_name.indexOf(".") + 1).equals("dll") || file_name.substring(file_name.indexOf(".") + 1).equals("txt")) return "Yes";
        else return "No";

    }
}

