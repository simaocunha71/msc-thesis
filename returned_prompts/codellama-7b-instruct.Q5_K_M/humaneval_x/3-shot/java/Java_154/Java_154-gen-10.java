        if (a == null || b == null || a.length() < b.length()) return false;

        for (int i = 0; i < a.length() - b.length() + 1; i++) {
            String substr = a.substring(i, i + b.length());
            if (b.equals(substr)) return true;
        }
        return false;
    }
}

