        if (b.length() == 0) {
            return false;
        }
        int j = 0;
        while (j < a.length() - b.length()) {
            if (a.substring(j, j + b.length()).contains(b)) {
                return true;
            }
            j++;
        }
        return false;
    }
}