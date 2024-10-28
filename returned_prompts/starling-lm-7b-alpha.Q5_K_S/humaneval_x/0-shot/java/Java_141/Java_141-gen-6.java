    boolean threeDigit = false;
    boolean oneDot = false;
    boolean oneLetter = false;
    boolean isExe = false;
    boolean isDll = false;
    boolean isTxt = false;

    for (int i = 0; i < file_name.length(); i++) {
        char c = file_name.charAt(i);
        if (c >= '0' && c <= '9') {
            if (threeDigit) {
                return "No";
            }
            threeDigit = true;
        }
        if (c == '.') {
            if (oneDot) {
                return "No";
            }
            oneDot = true;
        }
        if (c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z') {
            if (oneLetter) {
                return "No";
            }
            oneLetter = true;
        }
        if (file_name.length() == i + 1 && file_name.charAt(i) == '.') {
            return "No";
        }
        if (file_name.length() == i + 1 && (file_name.charAt(i) == 't' || file_name.charAt(i) == 'd' || file_name.charAt(i) == 'x')) {
            isTxt = true;
        }
        if (file_name.length() == i + 3 && (file_name.charAt(i + 1) == 'x' || file_name.charAt(i + 1) == 'e' || file_name.charAt(i + 1) == 'l' || file_name.charAt(i + 1) == 'l' || file_name.charAt(i + 2) == 'l' || file_name.charAt(i + 2) == 'e')) {
            isDll = true;
        }
        if (file_name.length() == i + 3 && (file_name.charAt(i + 1) == 't' || file_name.charAt(i + 1