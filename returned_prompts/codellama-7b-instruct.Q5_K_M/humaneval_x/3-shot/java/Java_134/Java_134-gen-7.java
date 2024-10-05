        if (txt.length() == 0) {
            return false;
        }

        char last_char = txt.charAt(txt.length() - 1);

        if (last_char >= 'a' && last_char <= 'z' || last_char >= 'A' && last_char <= 'Z') {
            if (txt.length() == 1) {
                return true;
            } else {
                int index = txt.lastIndexOf(' ');
                if (index == txt.length() - 2) {
                    return true;
                } else {
                    return false;
                }
            }
        } else {
            return false;
        }
    }
}

