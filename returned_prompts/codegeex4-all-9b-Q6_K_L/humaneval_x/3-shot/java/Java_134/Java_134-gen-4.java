        if (txt.isEmpty() || txt.charAt(txt.length() - 1) == ' ') return false;
        char c = txt.charAt(txt.length() - 1);
        return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z');
    }
}

