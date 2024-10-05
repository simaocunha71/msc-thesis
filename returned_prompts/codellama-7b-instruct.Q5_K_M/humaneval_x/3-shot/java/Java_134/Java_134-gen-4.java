        if (txt.length() == 0) {
            return false;
        }
        int last_idx = txt.length() - 1;
        if (!Character.isLetter(txt.charAt(last_idx))) {
            return false;
        }
        int space_idx = txt.lastIndexOf(" ");
        if (space_idx == -1) {
            return true;
        }
        return space_idx != last_idx;
    }
}

