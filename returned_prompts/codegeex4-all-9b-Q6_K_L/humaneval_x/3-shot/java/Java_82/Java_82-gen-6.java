        if (string.length() < 2) {
            return false;
        }
        for (int i = 2; i < string.length(); i++) {
            if (string.length() % i == 0) {
                return false;
            }
        }
        return true;
    }
}

