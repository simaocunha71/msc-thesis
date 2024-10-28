        if (x instanceof Double || y instanceof Double || z instanceof Double) return false;
        if (x.equals(y + z) || y.equals(x + z) || z.equals(x + y)) return true;
        return false;
    }
}

