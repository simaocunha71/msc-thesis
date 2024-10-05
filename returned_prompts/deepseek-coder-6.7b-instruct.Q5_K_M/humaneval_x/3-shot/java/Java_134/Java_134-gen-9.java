        if(txt.length() == 0) {
            return false;
        }
        char lastChar = txt.charAt(txt.length() - 1);
        if(Character.isLetter(lastChar)) {
            if(txt.length() == 1) {
                return true;
            } else {
                char secondLastChar = txt.charAt(txt.length() - 2);
                return !Character.isLetter(secondLastChar);
            }
        } else {
            return false;
        }
    }
}

