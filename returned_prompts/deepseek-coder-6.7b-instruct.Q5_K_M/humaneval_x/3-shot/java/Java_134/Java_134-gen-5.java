        if (txt.isEmpty()) return false;
        if (!Character.isLetter(txt.charAt(txt.length() - 1))) return false;

        if (txt.length() == 1) return true;

        return txt.charAt(txt.length() - 2) == ' ';
    }
}

