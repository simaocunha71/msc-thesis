        String[] split_string = file_name.split("\\.");
        if (split_string.length != 2) return "No";
        if (split_string[0].length() > 3) return "No";
        if (!Character.isLetter(split_string[0].charAt(0))) return "No";
        if (!(split_string[1].equals("txt") || split_string[1].equals("exe") || split_string[1].equals("dll"))) return "No";
        return "Yes";
    }
}

