        String[] ext = {"txt", "exe", "dll"};
        int count = 0;
        boolean flag = false;
        for (int i = 0; i < file_name.length(); i++) {
            if (file_name.charAt(i) >= 'a' && file_name.charAt(i) <= 'z') {
                flag = true;
            } else if (file_name.charAt(i) >= 'A' && file_name.charAt(i) <= 'Z') {
                flag = true;
            } else if (file_name.charAt(i) >= '0' && file_name.charAt(i) <= '9') {
                count++;
            }
            if (file_name.charAt(i) == '.') {
                break;
            }
        }
        if (!flag) {
            return "No";
        }
        String tmp = file_name.substring(file_name.indexOf('.') + 1);
        for (int i = 0; i < ext.length; i++) {
            if (tmp.equals(ext[i])) {
                if (count > 3) {
                    return "No";
                }
                return "Yes";
            }
        }
        return "No";
    }
}
































































































































































































