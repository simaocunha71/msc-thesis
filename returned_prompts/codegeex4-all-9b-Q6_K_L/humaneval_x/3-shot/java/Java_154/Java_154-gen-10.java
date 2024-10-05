        for (int i = 0; i < b.length(); i++) {
            String b_rotated = b.substring(i) + b.substring(0, i);
            if (a.contains(b_rotated)) return true;
        }
        return false;
    }
}

