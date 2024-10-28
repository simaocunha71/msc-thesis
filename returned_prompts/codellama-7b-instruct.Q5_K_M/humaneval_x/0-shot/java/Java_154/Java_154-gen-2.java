        for (int i = 0; i < a.length(); i++) {
            String s = a.substring(i, a.length());
            if (s.contains(b)) {
                return true;
            }
        }
        return false;
    }
}

