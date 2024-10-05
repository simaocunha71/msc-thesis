        if (a == null || b == null || a.length() == 0 || b.length() == 0) return false;

        String a_rotated = a;
        for (int i = 0; i < a.length() - 1; i++) {
            a_rotated = a_rotated.substring(1) + a_rotated.charAt(0);
            if (a_rotated.contains(b)) return true;
        }
        return false;
    }
}

