    int i = 0;
    int j = file_name.length() - 1;
    boolean isOneDot = false;
    boolean isValid = true;

    while (i < j && isValid) {
        if (file_name.charAt(i) == '.') {
            isOneDot = true;
        } else if (!Character.isLetter(file_name.charAt(i))) {
            isValid = false;
        }

        if (file_name.charAt(j) == '.') {
            isOneDot = true;
        } else if (!Character.isLetter(file_name.charAt(j))) {
            isValid = false;
        }

        i++;
        j--;
    }

    if (isOneDot == false) {
        isValid = false;
    }

    if (isValid && file_name.length() < 4) {
        isValid = false;
    }

    if (isValid && file_name.length() > 4) {
        String substring = file_name.substring(file_name.length() - 3);
        if (substring.charAt(0) != '.' || substring.charAt(1) != 'd' || substring.charAt(2) != 'l' || substring.charAt(3) != 'l') {
            isValid = false;
        }
    }

    if (isValid && file_name.length() > 4) {
        String substring2 = file_name.substring(0, 3);
        if (substring2.charAt(0) != '.' || substring2.charAt(1) != 't' || substring2.charAt(2) != 'x') {
            isValid = false;
        }
    }

    if (isValid && file_name.length() > 4) {
        String substring3 = file_name.substring(0, 3);
        if (substring3.charAt(0) != '.' || substring3.charAt(1) != 'e' || substring3.charAt(2) != 'x') {
            is