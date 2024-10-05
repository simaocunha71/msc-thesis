        int counter = 0;
        int dot = 0;
        boolean flag = false;
        if (file_name.length() < 3 || file_name.length() > 250) {
            return "No";
        }
        for (int i = 0; i < file_name.length(); i++) {
            if (file_name.charAt(i) >= 'A' && file_name.charAt(i) <= 'Z') {
                flag = true;
            } else if (file_name.charAt(i) >= 'a' && file_name.charAt(i) <= 'z') {
                flag = true;
            } else if (file_name.charAt(i) >= '0' && file_name.charAt(i) <= '9') {
                counter++;
            } else if (file_name.charAt(i) == '.') {
                dot++;
            } else {
                flag = false;
                break;
            }
        }
        if (counter > 3 || dot != 1) {
            return "No";
        }
        String[] substring = file_name.split("\\.");
        if (flag == false || !substring[1].equals("txt") && !substring[1].equals("exe") && !substring[1].equals("dll")) {
            return "No";
        }
        return "Yes";
    }
}







































































































































































