        for (int i = 0; i < a.length(); i++) {
            String bRotated = b + b.substring(0, i);
            if (a.contains(bRotated)) {
                return true;
            }
        }
        return false;
    }
}

