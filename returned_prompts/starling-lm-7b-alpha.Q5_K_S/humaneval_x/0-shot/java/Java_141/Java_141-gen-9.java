        int cnt = 0;
        boolean flag = false;
        for(int i = 0; i < file_name.length(); i++) {
            if(file_name.charAt(i) >= '0' && file_name.charAt(i) <= '9') {
                cnt++;
                if(cnt > 3) {
                    return "No";
                }
            } else if(file_name.charAt(i) == '.') {
                flag = true;
            } else {
                if(i == 0 && !(file_name.charAt(i) >= 'a' && file_name.charAt(i) <= 'z') && !(file_name.charAt(i) >= 'A' && file_name.charAt(i) <= 'Z')) {
                    return "No";
                }
            }
        }

        if(flag == false) {
            return "No";
        }

        String[] arr = file_name.split("\\.");
        if(arr.length != 2) {
            return "No";
        }

        if(arr[0].length() == 0 || arr[1].length() == 0) {
            return "No";
        }

        if(!(arr[1].equals("txt") || arr[1].equals("exe") || arr[1].equals("dll"))) {
            return "No";
        }

        return "Yes";

    }
}

























































































































































