        if (x instanceof Integer && y instanceof Integer && z instanceof Integer) {
            return (x.equals(y + z)) || (y.equals(z + x)) || (z.equals(x + y));
        } else {
            return false;
        }
    }
}

