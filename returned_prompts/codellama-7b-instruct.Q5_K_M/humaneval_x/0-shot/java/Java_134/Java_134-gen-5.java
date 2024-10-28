        //check if it's not empty
        if (txt.isEmpty()) {
            return false;
        }
        //check if last char is alphabetical
        if (Character.isAlphabetic(txt.charAt(txt.length() - 1))) {
            //check if last char is a part of a word
            if (txt.charAt(txt.length() - 1) != ' ') {
                return true;
            }
        }
        return false;
    }
}
