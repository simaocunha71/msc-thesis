        if (x instanceof Integer && y instanceof Integer && z instanceof Integer) {
            Integer xi = (Integer) x;
            Integer yi = (Integer) y;
            Integer zi = (Integer) z;
            return xi.equals(yi + zi) || yi.equals(xi + zi) || zi.equals(xi + yi);
        } else {
            return false;
        }
    }
}


