        for (int i = 0; i < a.length(); i++) {
            if (a.substring(i).contains(b)) {
                return true;
            }
            if (a.substring(0, i).contains(b)) {
                return true;
            }
        }
        return false;
    }
}

