        if (a == 0) return true;
        int cube_root = (int)Math.cbrt(Math.abs(a));
        return cube_root * cube_root * cube_root == a;
    }
}

