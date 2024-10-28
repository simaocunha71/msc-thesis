        if (txt.isEmpty()) return false;
        if (Character.isLetter(txt.charAt(txt.length() - 1))) {
            return txt.trim().endsWith(" " + txt.charAt(txt.length() - 1));
        }
        return false;
    }
}

