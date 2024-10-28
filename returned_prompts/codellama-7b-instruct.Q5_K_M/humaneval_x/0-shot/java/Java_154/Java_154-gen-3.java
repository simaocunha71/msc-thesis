        for (int i = 0; i < a.length(); i++) {
            if (a.contains(b)) {
                return true;
            }
            for (int j = 0; j < b.length(); j++) {
                b = b.substring(1) + b.charAt(0);
                if (a.contains(b)) {
                    return true;
                }
            }
        }
        return false;
    }
}
