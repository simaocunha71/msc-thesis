        if (a.indexOf(b) >= 0) return true;
        for (int i = 0; i < b.length(); i++) {
            b = b.charAt(b.length() - 1) + b.substring(0, b.length() - 1);
            if (a.indexOf(b) >= 0) return true;
        }
        return false;
    }
}

