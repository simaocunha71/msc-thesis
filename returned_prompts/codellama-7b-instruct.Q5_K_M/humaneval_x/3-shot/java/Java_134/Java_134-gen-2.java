        if (txt.length() == 0) return false;
        if (txt.charAt(txt.length() - 1) >= 'A' && txt.charAt(txt.length() - 1) <= 'Z') return true;
        if (txt.charAt(txt.length() - 1) >= 'a' && txt.charAt(txt.length() - 1) <= 'z') return true;
        return false;
    }
}

