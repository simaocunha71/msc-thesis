        if (txt.isEmpty()) return false;
        int lastIndex = txt.length() - 1;
        if (!Character.isLetter(txt.charAt(lastIndex))) return false;
        if (lastIndex > 0 && txt.charAt(lastIndex - 1) == ' ') return false;
        return true;
    }
}

