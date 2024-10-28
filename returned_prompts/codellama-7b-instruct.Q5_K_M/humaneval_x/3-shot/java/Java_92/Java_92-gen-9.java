        if (!(x instanceof Integer) || !(y instanceof Integer) || !(z instanceof Integer)) return false;
        if (x == y + z) return true;
        return false;
    }
}

