        if (x instanceof Integer && y instanceof Integer && z instanceof Integer) {
            if (x.equals(y + z)) {
                return true;
            } else if (y.equals(x + z)) {
                return true;
            } else if (z.equals(x + y)) {
                return true;
            } else {
                return false;
            }
        } else {
            return false;
        }
    }
}








```
