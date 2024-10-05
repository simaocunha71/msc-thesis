        String b_rotated = b + b;
        return a.contains(b) || a.contains(b_rotated.substring(1));
    }
}

