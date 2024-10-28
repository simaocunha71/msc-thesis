        if (x instanceof Double || y instanceof Double || z instanceof Double) return false;
        if (x.equals(y + z)) return true;
        else return false;
    }
}

