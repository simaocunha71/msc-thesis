        if (!(x instanceof Integer) || !(y instanceof Integer) || !(z instanceof Integer)) return false;

        int xi = (int) x;
        int yi = (int) y;
        int zi = (int) z;

        if (xi == yi + zi) return true;
        else return false;
    }
}

