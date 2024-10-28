        if (!(x instanceof Integer) || !(y instanceof Integer) || !(z instanceof Integer)) {
            return false;
        }
        if (((int) x + (int) y == (int) z) || ((int) x + (int) z == (int) y) || ((int) y + (int) z == (int) x)) {
            return true;
        }
        return false;

    }
}