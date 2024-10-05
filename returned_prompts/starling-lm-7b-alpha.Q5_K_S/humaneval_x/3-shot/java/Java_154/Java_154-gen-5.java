        for (int i = 0; i < b.length(); i++) {
            for (int j = i; j < b.length(); j++) {
                String rotated = b.substring(j) + b.substring(0, j);
                if (a.contains(rotated)) {
                    return true;
                }
            }
        }
        return false;
    }
}

