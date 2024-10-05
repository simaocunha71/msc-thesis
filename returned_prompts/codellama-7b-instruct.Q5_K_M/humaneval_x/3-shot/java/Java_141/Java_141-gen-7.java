        if (file_name.length() > 3) return "No";
        if (file_name.split("\\.").length != 2) return "No";
        if (file_name.split("\\.")[0].length() == 0) return "No";
        if (!Character.isLetter(file_name.split("\\.")[0].charAt(0))) return "No";
        if (!file_name.split("\\.")[1].equals("txt") &&
                !file_name.split("\\.")[1].equals("exe") &&
                !file_name.split("\\.")[1].equals("dll")) return "No";
        return "Yes";

    }
}

