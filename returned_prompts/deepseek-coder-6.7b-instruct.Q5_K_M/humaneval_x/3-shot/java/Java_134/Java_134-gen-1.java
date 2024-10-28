        if(txt.isEmpty()) return false;

        char lastChar = txt.charAt(txt.length() - 1);
        if(Character.isLetter(lastChar)) {
            if(txt.length() == 1) {
                return true;
            } else {
                char secondToLastChar = txt.charAt(txt.length() - 2);
                return !Character.isLetter(secondToLastChar);
            }
        } else {
            return false;
        }

     }
}

