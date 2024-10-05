        if (x instanceof Integer && y instanceof Integer && z instanceof Integer) {
            Integer a = (Integer) x;
            Integer b = (Integer) y;
            Integer c = (Integer) z;
            return a + b == c || b + c == a || a + c == b;
        } else {
            return false;
        }
    }
}

