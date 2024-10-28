        if (!a.contains(b)) return false;

        for (int i = 0; i < a.length(); i++) {
            String rotated = a.substring(i) + a.substring(0, i);
            if (rotated.contains(b)) return true;
        }
        return false;
    }
}

