        if (txt.length() == 0) return false;
        char last_char = txt.charAt(txt.length() - 1);
        if (!Character.isLetter(last_char)) return false;
        int index = txt.lastIndexOf(' ');
        return index == -1 || index == txt.length() - 1;
    }
}

