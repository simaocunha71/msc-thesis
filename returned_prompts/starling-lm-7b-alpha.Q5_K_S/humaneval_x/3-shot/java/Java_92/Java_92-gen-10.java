        if (x instanceof Integer && y instanceof Integer && z instanceof Integer) {
            Integer xi = (Integer) x;
            Integer yi = (Integer) y;
            Integer zi = (Integer) z;

            return (xi + yi == zi) || (xi + zi == yi) || (yi + zi == xi);
        }
        return false;
    }
}

