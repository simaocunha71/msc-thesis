        if (txt.length() == 0) return false;
        String last_char = txt.substring(txt.length() - 1);
        if (Character.isLetter(last_char.charAt(0)) && !Character.isAlphabetic(last_char.charAt(0))) return true;
        else return false;
    }
}

