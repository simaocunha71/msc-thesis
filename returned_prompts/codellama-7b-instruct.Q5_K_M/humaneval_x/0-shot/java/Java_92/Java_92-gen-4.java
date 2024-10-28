        if (x instanceof Integer && y instanceof Integer && z instanceof Integer) {
            int ix = (int) x;
            int iy = (int) y;
            int iz = (int) z;
            if (ix + iy == iz || iy + iz == ix || iz + ix == iy) {
                return true;
            }
        }

        return false;
    }
}
