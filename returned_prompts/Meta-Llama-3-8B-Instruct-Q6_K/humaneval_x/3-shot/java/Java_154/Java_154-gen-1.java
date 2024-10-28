        if (a.length() < b.length()) {
            return false;
        }
        for (int i = 0; i < a.length(); i++) {
            if (a.substring(i).contains(b)) {
                return true;
            }
        }
        return false;
    }
}

