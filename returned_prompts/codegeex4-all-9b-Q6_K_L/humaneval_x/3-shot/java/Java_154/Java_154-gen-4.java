        for (int i = 0; i < a.length() - b.length() + 1; i++) {
            if (a.substring(i, i + b.length()).equals(b)) {
                return true;
            }
            if (a.substring(i, i + b.length()).equals(b.substring(1) + b.substring(0, 1))) {
                return true;
            }
        }
        return false;
    }
}

