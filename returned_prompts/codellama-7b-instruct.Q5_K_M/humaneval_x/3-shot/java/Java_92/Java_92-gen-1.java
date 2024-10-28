        if (!(x instanceof Integer) || !(y instanceof Integer) || !(z instanceof Integer)) return false;
        if (((int) x) == ((int) y) + ((int) z)) return true;
        return false;
    }
}

